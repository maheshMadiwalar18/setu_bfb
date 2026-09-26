import React, { useEffect, useRef } from 'react';
import { ChatMessage } from '../../types';
import { Bot, User, Wrench, CheckCircle2, ShieldAlert } from 'lucide-react';

interface ChatMessagesProps {
  messages: ChatMessage[];
  isStreaming: boolean;
}

export const ChatMessages: React.FC<ChatMessagesProps> = ({ messages, isStreaming }) => {
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages, isStreaming]);

  return (
    <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-5">
      {messages.map((msg) => {
        const isUser = msg.role === 'user';

        return (
          <div
            key={msg.id}
            className={`flex items-start gap-3 ${isUser ? 'justify-end' : 'justify-start'} animate-fade-in`}
          >
            {/* AI Avatar */}
            {!isUser && (
              <div className="w-8 h-8 rounded-full bg-setu-blue text-white flex items-center justify-center flex-shrink-0 font-serif font-bold text-xs shadow-xs border border-white/20">
                सेतु
              </div>
            )}

            {/* Bubble Content */}
            <div className={`max-w-[82%] sm:max-w-[75%] space-y-2`}>
              {/* Tool Execution Box (if present) */}
              {msg.tool_call && (
                <div className="bg-slate-100 border border-slate-200 rounded-lg p-2.5 text-[11px] text-slate-700 flex items-center space-x-2 font-mono shadow-2xs">
                  <Wrench className="w-3.5 h-3.5 text-setu-saffron flex-shrink-0" />
                  <span>Executing Tool: <strong>{msg.tool_call.tool}</strong></span>
                </div>
              )}

              {/* Message Bubble */}
              <div
                className={`p-3.5 sm:p-4 rounded-2xl text-xs sm:text-sm leading-relaxed shadow-xs ${
                  isUser
                    ? 'bg-setu-blue text-white rounded-tr-none font-medium'
                    : 'bg-white text-slate-800 border border-slate-200 rounded-tl-none'
                }`}
              >
                <div className="whitespace-pre-line break-words">{msg.content}</div>
              </div>

              {/* Timestamp */}
              <div
                className={`text-[10px] text-slate-400 px-1 ${
                  isUser ? 'text-right' : 'text-left'
                }`}
              >
                {msg.timestamp}
              </div>
            </div>

            {/* User Avatar */}
            {isUser && (
              <div className="w-8 h-8 rounded-full bg-slate-200 text-slate-700 flex items-center justify-center flex-shrink-0 shadow-xs">
                <User className="w-4 h-4" />
              </div>
            )}
          </div>
        );
      })}

      {/* Typing Indicator */}
      {isStreaming && (
        <div className="flex items-start gap-3 justify-start animate-fade-in">
          <div className="w-8 h-8 rounded-full bg-setu-blue text-white flex items-center justify-center flex-shrink-0 font-serif font-bold text-xs shadow-xs">
            सेतु
          </div>
          <div className="bg-white border border-slate-200 p-3.5 rounded-2xl rounded-tl-none shadow-xs flex items-center space-x-1.5">
            <span className="w-2 h-2 rounded-full bg-setu-blue animate-bounce" style={{ animationDelay: '0ms' }} />
            <span className="w-2 h-2 rounded-full bg-setu-blue animate-bounce" style={{ animationDelay: '150ms' }} />
            <span className="w-2 h-2 rounded-full bg-setu-blue animate-bounce" style={{ animationDelay: '300ms' }} />
          </div>
        </div>
      )}

      <div ref={bottomRef} />
    </div>
  );
};
