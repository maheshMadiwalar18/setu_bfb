# API Documentation

Base URL: `http://localhost:8000/api`

## Chat API

### `POST /chat`
Main AI interaction endpoint using Server-Sent Events (SSE).

**Request Body:**
```json
{
  "message": "I need a scholarship for my daughter",
  "language": "en",
  "conversation_history": [],
  "user_profile": {
    "state": "Karnataka"
  }
}
```

**Response (text/event-stream):**
Streams chunks of data containing text, tool calls, tool results, UI actions, and suggestions.

## Schemes API

### `GET /schemes`
Search and filter schemes from the database.

**Query Parameters:**
- `q`: Search query
- `category`: Filter by category
- `state`: Filter by state
- `page`: Page number (default 1)

**Response:**
```json
{
  "total": 30,
  "page": 1,
  "limit": 20,
  "schemes": [
    {
      "id": "pm-kisan",
      "name": "PM Kisan Samman Nidhi",
      "benefit_amount": "₹6,000/year"
    }
  ]
}
```

## Government Scraper API

### `GET /gov-schemes/search`
Live web scraping from myscheme.gov.in.

**Response:**
```json
{
  "schemes": [
    {
      "title": "...",
      "description": "...",
      "apply_url": "..."
    }
  ]
}
```

### `GET /gov-schemes/portals`
Returns a curated directory of official government portals.

## Wizard API

### `POST /wizard/match`
Calculates eligibility scores.

**Request Body:**
```json
{
  "age": 35,
  "gender": "female",
  "state": "Karnataka",
  "income_annual": 180000,
  "needs": ["education"]
}
```

**Response:**
```json
{
  "total_matched": 5,
  "schemes": [
    {
      "name": "Scheme A",
      "match_percentage": 98
    }
  ]
}
```

## CSC API

### `POST /csc/login`
Authenticates a Common Service Centre Operator.

**Request Body:**
```json
{
  "operator_id": "operator@csc.gov.in",
  "password": "demo123"
}
```
