# 🤖 AI Customer Support Agent

An AI-powered customer support agent that processes e-commerce refund requests using **FastAPI**, **LangGraph**, **Groq Llama 3.1**, **SQLite**, and **React**.

The agent validates customer details, order information, and refund policy before making a structured refund decision. Every decision is logged along with the agent's reasoning trace for transparency.

---

## Features

- AI-powered refund approval/denial
- LangGraph-based agent workflow
- Structured LLM output using Groq Llama 3.1
- SQLite CRM database
- Refund policy validation
- Customer refund interface
- Admin dashboard
- Refund history logs
- Agent reasoning trace
- FastAPI Swagger documentation

---

## Tech Stack

### Backend

- FastAPI
- LangGraph
- LangChain
- Groq API (Llama 3.1 8B Instant)
- SQLite
- Pandas

### Frontend

- React
- Vite
- JavaScript

---

## Project Structure

```
AI_custom_support_agent/

├── Backend/
│   ├── agents/
│   ├── graphs/
│   ├── routes/
│   ├── services/
│   ├── tools/
│   ├── schemas/
│   ├── app.py
│   └── database.py
│
├── Database/
│   ├── ecommerce.db
│   └── init_db.py
│
├── Data/
│   ├── customers.csv
│   ├── orders.csv
│   └── refund_policy.txt
│
├── Frontend/
│   └── src/
│       ├── components/
│       ├── dashboard/
│       ├── pages/
│       └── hooks/
│
├── Test/
├── requirements.txt
└── README.md
```

---

## Architecture

```
React Frontend
        │
        ▼
    FastAPI APIs
        │
        ▼
   LangGraph Agent
        │
 ┌──────┴────────┐
 ▼               ▼
SQLite      Refund Policy
 Database         TXT
        │
        ▼
 Groq Llama 3.1
        │
        ▼
 Structured Decision
        │
        ▼
 Refund Logs
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/customer/{id}` | Get customer |
| GET | `/order/{id}` | Get order |
| GET | `/policy` | Get refund policy |
| POST | `/refund` | Process refund |
| GET | `/refund/logs` | View refund history |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Sucheta-d/AI-Customer-Support-Agent.git
cd AI-Customer-Support-Agent
```

Install backend dependencies:

```bash
uv sync
```

or

```bash
pip install -r requirements.txt
```

Start the backend:

```bash
uvicorn Backend.app:app --reload
```

Start the frontend:

```bash
cd Frontend
npm install
npm run dev
```

---

## Swagger Documentation

Open:

```
http://localhost:8000/docs
```

---

## Sample Refund Response

```json
{
  "customer_id": 1,
  "order_id": 101,
  "decision": "APPROVED",
  "reason": "Damaged product received, within refund period, and eligible for refund.",
  "trace": [
    "Loading customer",
    "Loading order",
    "Loading refund policy",
    "Calling Llama 3.1",
    "Decision generated"
  ]
}
```

---

## Future Improvements

- Voice-enabled customer support
- Authentication
- Live dashboard updates using WebSockets
- Docker deployment
- Cloud database
- CI/CD pipeline

---

## Author

**Sucheta Dawn**

GitHub: https://github.com/Sucheta-d