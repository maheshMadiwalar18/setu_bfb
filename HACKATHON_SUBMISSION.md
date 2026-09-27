# SETU - Hackathon Submission

**Tagline:** One Voice. Every Service.

## 🚀 The Problem
Over 800 million rural and semi-urban Indian citizens struggle to access government welfare schemes. The barriers are immense:
1. **Fragmentation:** 700+ schemes spread across 50+ central and state portals.
2. **Language:** Portals are often English-first or use highly formal Hindi.
3. **UI Complexity:** Complex forms and navigation deter low-digital-literacy users.
4. **Eligibility Confusion:** Citizens don't know what they qualify for.

## 💡 The Solution: SETU
SETU (सेतु) bridges the gap between citizens and the government. It is an AI-powered, voice-first platform that speaks 12 Indian languages.

Instead of forcing users to search through menus, SETU asks: *"How can I help you today?"* 
A citizen simply speaks: *"I need a scholarship for my daughter,"* and SETU handles the rest.

## ✨ Key Features Developed
- **Conversational AI Agent:** Built with Claude tool-calling architecture.
- **Multilingual Web Speech:** Native voice-to-text in local dialects.
- **Live Scraper Engine:** Real-time data extraction from myscheme.gov.in.
- **Eligibility Wizard:** 4-step wizard calculating match probabilities.
- **DigiLocker Mock:** Simulated OAuth flow for DBT payment status.
- **CSC Operator Portal:** A dedicated dashboard for Village Level Entrepreneurs to assist citizens.

## 🏗️ Architecture
- **Frontend:** React 18, Vite, Tailwind CSS, Lucide Icons, react-i18next.
- **Backend:** FastAPI, Python, SQLAlchemy, Server-Sent Events (SSE).
- **Database:** SQLite (PostgreSQL compatible).
- **AI:** OpenRouter (Claude Sonnet 5) + Deterministic Fallback Engine.

## 📈 Impact
SETU reduces scheme discovery time from **hours to seconds**. By providing a conversational, voice-first interface, it democratizes access to welfare, ensuring that no eligible citizen is left behind due to digital or linguistic barriers.

## 📸 Local Setup
```bash
git clone https://github.com/maheshMadiwalar18/setu_bfb.git
cd setu_bfb
.\start.bat
```
Visit `http://localhost:5173` to experience SETU.
