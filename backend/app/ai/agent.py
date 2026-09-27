import json
import logging
from typing import AsyncGenerator, Dict, Any, List
from sqlalchemy.orm import Session
from app.config import settings
from app.ai.tools import execute_tool, ANTHROPIC_TOOLS
from app.ai.fallback_engine import stream_ai_response as stream_fallback_engine, SYSTEM_PROMPT

logger = logging.getLogger("setu.ai")

LANG_NAMES = {
    "hi": "Hindi (हिन्दी)",
    "kn": "Kannada (ಕನ್ನಡ)",
    "ta": "Tamil (தமிழ்)",
    "te": "Telugu (తెలుగు)",
    "mr": "Marathi (मराठी)",
    "ml": "Malayalam (മലയാളം)",
    "bn": "Bengali (বাংলা)",
    "gu": "Gujarati (ગુજરાતી)",
    "pa": "Punjabi (ਪੰਜਾਬੀ)",
    "ur": "Urdu (اردو)",
    "or": "Odia (ଓଡ଼ିଆ)",
    "en": "English"
}

async def chat_stream(
    message: str,
    language: str,
    conversation_history: List[Dict[str, str]],
    user_profile: Dict[str, Any],
    db: Session
) -> AsyncGenerator[str, None]:
    """
    Main entry point for AI Chat. Uses Claude/OpenRouter if API key is available,
    otherwise uses the built-in deterministic multilingual engine.
    """
    api_key = settings.OPENROUTER_API_KEY or settings.ANTHROPIC_API_KEY
    is_openrouter = bool(settings.OPENROUTER_API_KEY and settings.OPENROUTER_API_KEY.strip())
    
    target_lang_name = LANG_NAMES.get(language, language)
    active_system_prompt = (
        f"{SYSTEM_PROMPT}\n\n"
        f"CRITICAL MULTILINGUAL INSTRUCTION: The citizen has explicitly selected the language '{target_lang_name}'. "
        f"You MUST formulate your response in {target_lang_name} using correct native script and respectful phrasing. "
        f"Do NOT default to English unless the selected language is English."
    )

    if api_key and api_key.strip() != "":
        try:
            if is_openrouter:
                import openai
                from app.ai.tools import OPENAI_TOOLS
                client = openai.AsyncOpenAI(
                    api_key=api_key,
                    base_url="https://openrouter.ai/api/v1",
                )
                model_name = "anthropic/claude-sonnet-5"

                # Build messages list for OpenAI
                messages = [{"role": "system", "content": active_system_prompt}]
                for m in conversation_history:
                    role = "user" if m.get("role") == "user" else "assistant"
                    messages.append({"role": role, "content": m.get("content", "")})
                messages.append({"role": "user", "content": message})

                # Call OpenAI with tools
                response = await client.chat.completions.create(
                    model=model_name,
                    messages=messages,
                    tools=OPENAI_TOOLS,
                    tool_choice="auto",
                    max_tokens=500,
                )

                message_obj = response.choices[0].message

                if message_obj.tool_calls:
                    messages.append(message_obj)
                    
                    for tool_call in message_obj.tool_calls:
                        tool_name = tool_call.function.name
                        tool_input = json.loads(tool_call.function.arguments)

                        yield f"data: {json.dumps({'type': 'tool_call', 'tool': tool_name, 'input': tool_input})}\n\n"

                        tool_res = execute_tool(tool_name, tool_input, db)
                        yield f"data: {json.dumps({'type': 'tool_result', 'data': tool_res})}\n\n"

                        # Handle contextual right-panel actions
                        if tool_name == "search_schemes":
                            schemes = tool_res.get("schemes", [])
                            yield f"data: {json.dumps({'type': 'action', 'action': 'show_schemes', 'data': {'schemes': schemes, 'count': len(schemes)}})}\n\n"
                        elif tool_name == "check_payment_status":
                            if tool_input.get("requires_digilocker") and not (user_profile and user_profile.get("digilocker_verified")):
                                yield f"data: {json.dumps({'type': 'action', 'action': 'show_digilocker_prompt', 'data': {'scheme_name': tool_input.get('scheme_name')}})}\n\n"
                        elif tool_name == "get_required_documents":
                            yield f"data: {json.dumps({'type': 'action', 'action': 'show_document_checklist', 'data': tool_res})}\n\n"
                        elif tool_name == "check_eligibility":
                            yield f"data: {json.dumps({'type': 'action', 'action': 'show_eligibility_breakdown', 'data': tool_res})}\n\n"

                        # Append each tool result
                        messages.append({
                            "role": "tool",
                            "tool_call_id": tool_call.id,
                            "name": tool_name,
                            "content": json.dumps(tool_res)
                        })

                    # Second turn (only happens once after all tools are executed)
                    followup = await client.chat.completions.create(
                        model=model_name,
                        messages=messages,
                        max_tokens=500,
                    )

                    followup_text = followup.choices[0].message.content or ""
                    for chunk in followup_text.split(" "):
                        yield f"data: {json.dumps({'type': 'text', 'content': chunk + ' '})}\n\n"

                elif message_obj.content:
                    for chunk in message_obj.content.split(" "):
                        yield f"data: {json.dumps({'type': 'text', 'content': chunk + ' '})}\n\n"

                yield f"data: {json.dumps({'type': 'done'})}\n\n"
                return

            else:
                import anthropic
                
                client = anthropic.AsyncAnthropic(api_key=api_key)
                model_name = settings.CLAUDE_MODEL

                # Build messages list
                messages = []
                for m in conversation_history:
                    role = "user" if m.get("role") == "user" else "assistant"
                    messages.append({"role": role, "content": m.get("content", "")})
                messages.append({"role": "user", "content": message})

                # Call Anthropic with tools
                response = await client.messages.create(
                    model=model_name,
                    max_tokens=1024,
                    system=active_system_prompt,
                    tools=ANTHROPIC_TOOLS,
                    messages=messages
                )

                # Check if tools were called
                for content_block in response.content:
                    if content_block.type == "tool_use":
                        tool_name = content_block.name
                        tool_input = content_block.input
                        
                        yield f"data: {json.dumps({'type': 'tool_call', 'tool': tool_name, 'input': tool_input})}\n\n"
                        
                        tool_res = execute_tool(tool_name, tool_input, db)
                        yield f"data: {json.dumps({'type': 'tool_result', 'data': tool_res})}\n\n"

                        # Handle contextual right-panel actions
                        if tool_name == "search_schemes":
                            schemes = tool_res.get("schemes", [])
                            yield f"data: {json.dumps({'type': 'action', 'action': 'show_schemes', 'data': {'schemes': schemes, 'count': len(schemes)}})}\n\n"
                        elif tool_name == "check_payment_status":
                            if tool_input.get("requires_digilocker") and not (user_profile and user_profile.get("digilocker_verified")):
                                yield f"data: {json.dumps({'type': 'action', 'action': 'show_digilocker_prompt', 'data': {'scheme_name': tool_input.get('scheme_name')}})}\n\n"
                        elif tool_name == "get_required_documents":
                            yield f"data: {json.dumps({'type': 'action', 'action': 'show_document_checklist', 'data': tool_res})}\n\n"
                        elif tool_name == "check_eligibility":
                            yield f"data: {json.dumps({'type': 'action', 'action': 'show_eligibility_breakdown', 'data': tool_res})}\n\n"

                        # Second turn to summarize tool result
                        followup = await client.messages.create(
                            model=model_name,
                            max_tokens=1024,
                            system=active_system_prompt,
                            tools=ANTHROPIC_TOOLS,
                            messages=messages + [
                                {"role": "assistant", "content": [{"type": "tool_use", "id": content_block.id, "name": tool_name, "input": tool_input}]},
                                {"role": "user", "content": [{"type": "tool_result", "tool_use_id": content_block.id, "content": json.dumps(tool_res)}]}
                            ]
                        )

                        for b in followup.content:
                            if b.type == "text":
                                for chunk in b.text.split(" "):
                                    yield f"data: {json.dumps({'type': 'text', 'content': chunk + ' '})}\n\n"

                    elif content_block.type == "text":
                        for chunk in content_block.text.split(" "):
                            yield f"data: {json.dumps({'type': 'text', 'content': chunk + ' '})}\n\n"

                yield f"data: {json.dumps({'type': 'done'})}\n\n"
                return

        except Exception as e:
            logger.warning(f"Claude API failed: {e}. Falling back to deterministic multilingual engine.")
            # Fall through to fallback engine

    # Built-in deterministic multilingual engine
    async for chunk in stream_fallback_engine(message, language, conversation_history, user_profile, db):
        yield chunk
