# SETU (सेतु) — One Voice. Every Service.

> **National AI-Powered Government Schemes Discovery Portal**  
> *A production-ready prototype empowering Indian citizens to discover, verify, and access government welfare entitlements through natural conversation in 12 Indian languages.*

---

## 🏛️ Brand & Identity
- **Name**: SETU (सेतु)
- **Tagline**: One Voice. Every Service.
- **Brand Colors**:
  - Primary Blue: `#1A3A6B`
  - Saffron Accent: `#FF6B00`
  - India Green: `#138808`
  - Background: `#F5F7FA`
  - White: `#FFFFFF`
- **Typography**: Noto Sans (Devanagari, Kannada, Tamil, Telugu, and Pan-Indian scripts)
- **Zero-Emoji Policy**: Strictly SVG icons (Lucide Icons) and official Indian script typography throughout all UI elements and responses.

---

## 🚀 Quick Start

### 1. One-Click Launch (Windows)
Double-click or run:
```bash
.\start.bat
```

### 2. Manual Start

#### Backend (FastAPI + SQLAlchemy + Claude Tool Calling):
```bash
cd backend
py -m pip install -r requirements.txt
py run.py
```
*Backend runs on `http://localhost:8000` (Docs: `http://localhost:8000/docs`)*

#### Frontend (React 18 + TypeScript + Vite + Tailwind CSS):
```bash
cd frontend
npm install
npm run dev
```
*Frontend runs on `http://localhost:5173`*

---

## 🔑 Key Features & User Flows

| Route | Page | Description |
|---|---|---|
| `/` | **Home Page** | Accessibility bar (A-/A+, contrast), large voice search bar (Web Speech API), 12 category cards, animated stats, interactive SVG India state map, popular schemes horizontal scroll. |
| `/find` | **Eligibility Wizard** | 4-step progressive questionnaire (Age, Gender, State, Income slider, Social category, BPL, Needs) with real-time match scoring and detailed eligibility criteria checklist modal. |
| `/schemes` | **Scheme Listing** | Directory with search bar, sidebar filters (Categories, States, Central/State, Benefit types, Online/Offline), sorting, and skeleton loaders. |
| `/schemes/:id` | **Scheme Detail** | 6 functional tabs (Overview, Eligibility, Benefits, Documents Required with PDF checklist download, How to Apply, FAQs), quick info card, and official external portal links. |
| `/chat` | **SETU AI Assistant** | Realtime Server-Sent Events (SSE) chat with voice input, dynamic 5-state right context panel (Idle, Schemes, Docs checklist, DigiLocker OAuth, Eligibility breakdown). |
| `/csc` | **CSC Operator Portal** | Village Level Entrepreneur dashboard (`operator@csc.gov.in` / `demo123`), daily stats, recent citizen assistance logs, on-behalf intake mode, and printable citizen summary reports. |
| `/about` | **About Platform** | Mission, governance standards, GIGW / WCAG 2.0 AA compliance, and participating ministries. |

---

## 🧪 Verified User Scenarios

1. **Voice Search from Home**: Click mic on home page -> speak requirement (e.g. *"scholarship for my daughter in college"*) -> auto-fills & redirects to `/chat` with AI scheme recommendations.
2. **Eligibility Wizard**: Fill 35-yr female in Karnataka with Rs 1.8L income -> Gruha Lakshmi matches with 98% score -> click *"Check Eligibility"* for green checkmark breakdown.
3. **Payment Status & DigiLocker**: Ask in chat *"Did I get my Gruha Lakshmi money this month?"* -> triggers DigiLocker permission card -> click *"Connect DigiLocker"* -> instant verified DBT credit response (Rs 2,000 to A/C ending 7834 on 15 Nov 2024).

---

## 🛠️ Tech Stack & Architecture

- **Frontend**: Next.js / Vite React 18, TypeScript, Tailwind CSS, Lucide Icons, `react-i18next`.
- **Backend**: FastAPI (Python), SQLAlchemy (SQLite zero-config out of the box + PostgreSQL compatible), Redis caching layer with in-memory fallback, SSE streaming.
- **AI Intelligence**: OpenAI GPT-4o / Anthropic Claude tool-calling gateway with deterministic synthesis engine fallback ensuring 100% operational uptime.
- **Compliance & Standards**: GIGW & WCAG 2.0 AA standard compliance.

