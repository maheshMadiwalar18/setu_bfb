# Architecture

SETU is built on a modern, decoupled architecture designed for scalability, low latency, and high availability.

## High-Level Architecture

```mermaid
graph TB
    subgraph "Client Layer"
        U["👤 Citizen / CSC Operator"]
        B["🌐 Browser (Web Speech API)"]
    end
    
    subgraph "Frontend (React + Vite)"
        FE["React 18 SPA"]
        PAGES["Pages (13 Routes)"]
        COMP["Components (17 Modules)"]
        SVC["API Service Layer"]
        I18N["i18n (12 Languages)"]
        FB["Firebase Auth + Analytics"]
    end
    
    subgraph "Backend (FastAPI)"
        API["FastAPI Server"]
        R_SCHEMES["Schemes API"]
        R_CHAT["Chat API (SSE)"]
        R_WIZARD["Wizard API"]
        R_GOV["Gov Scraper API"]
    end
    
    subgraph "AI & Intelligence Layer"
        AGENT["AI Agent Router"]
        TOOLS["Tool Executor"]
        FALLBACK["Fallback Engine"]
    end
    
    subgraph "Data Layer"
        DB["SQLite Database"]
        CACHE["Redis Cache"]
    end
    
    U --> B --> FE
    FE --> SVC --> API
    API --> R_CHAT --> AGENT
    API --> R_SCHEMES --> DB
    API --> R_WIZARD --> DB
    API --> R_GOV --> |Scrape| EXTERNAL_GOV["myscheme.gov.in"]
    
    AGENT --> TOOLS --> DB
    AGENT --> FALLBACK
```

## Frontend Architecture
The frontend is a React 18 Single Page Application built with Vite and TypeScript.
- **State Management**: React Hooks (useState, useEffect, useContext).
- **Styling**: Tailwind CSS for responsive, utility-first styling.
- **Routing**: `react-router-dom` with 13 distinct routes.
- **Internationalization**: `react-i18next` handling 12 Indian languages.
- **Voice**: Native browser Web Speech API for voice-to-text.

## Backend Architecture
The backend is a FastAPI Python application.
- **Asynchronous**: Built on ASGI (Uvicorn) for high concurrency.
- **Streaming**: Server-Sent Events (SSE) used for real-time AI chat streaming.
- **Scraping**: `BeautifulSoup4` and `lxml` for real-time data extraction from government portals.
- **ORM**: SQLAlchemy 2.0 interacting with a SQLite database (PostgreSQL compatible).

## AI Architecture
SETU uses a sophisticated tool-calling AI architecture.

```mermaid
graph TD
    Input["User Query"] --> LangDetect["Language Detection"]
    LangDetect --> Router{"API Key Present?"}
    
    Router -->|Yes| LLM["Claude / OpenRouter"]
    Router -->|No| Fallback["Deterministic Fallback Engine"]
    
    LLM --> Decision{"Needs Tool?"}
    Decision -->|Yes| Tools["Execute Tool"]
    Decision -->|No| Format["Format Response"]
    
    Fallback --> IntentMatch["Regex/Intent Matching"]
    IntentMatch --> Tools
    
    Tools --> DB["Database Query"]
    DB --> Tools
    Tools --> Format
    Format --> Output["SSE Stream to Client"]
```
