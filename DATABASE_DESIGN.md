# Database Design

SETU uses SQLite out-of-the-box via SQLAlchemy 2.0, making it fully PostgreSQL compatible for production deployment.

## Entity Relationship Diagram

```mermaid
erDiagram
    SCHEMES {
        string id PK
        string code UK
        string name 
        string category 
        string state 
        string ministry 
        text summary 
        string benefit_amount 
        string apply_url 
        int min_age 
        int max_age 
        float income_ceiling 
        json documents_required 
        json application_steps 
        datetime created_at
    }
    
    GRIEVANCES {
        string id PK 
        string scheme_name 
        string issue_type 
        text description 
        string citizen_name 
        string status 
        datetime created_at
    }
    
    CSC_USERS {
        int id PK 
        string operator_id UK 
        string center_code
        string name
        string state
        int today_assisted_count
    }
    
    CITIZEN_QUERIES {
        int id PK 
        string citizen_name 
        string phone 
        json matched_schemes 
        bool assisted_by_csc 
        datetime created_at
    }
    
    CSC_USERS ||--o{ CITIZEN_QUERIES : "assists"
```

## Tables

### 1. Schemes Table
Stores curated scheme data with detailed eligibility criteria (age, gender, state, income, BPL status) used by the AI tool and Wizard for deterministic matching.

### 2. Grievances Table
Stores citizen complaints (e.g., payment not received, application rejected) generated via the AI chat interface.

### 3. CSC_Users Table
Stores Village Level Entrepreneur (VLE) profiles for the CSC dashboard.

### 4. Citizen_Queries Table
Logs intake sessions performed by CSC operators on behalf of citizens, including the matched schemes for auditing.
