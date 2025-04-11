# 🔍 Solvei8 AI Internship Assignment: Booking Analytics & LLM Q&A System

I have developed a system that processes hotel booking data, extracts insights, and enables retrieval-augmented question answering (RAG). The system will provide analytics as mentioned in below sections and answer user queries about the data.

## 🌟 Features

- ✅ Natural language question-answering over real hotel booking data
- ✅ FastAPI backend with `/ask` and `/analytics` endpoints
- ✅ Integration with OpenRouter (GPT-3.5-turbo)
- ✅ Analytics-ready data from a real-world dataset
- ✅ CORS enabled for frontend integrations
- ✅ API tested via Swagger UI, curl, and Postman
- ✅ Performance evaluation with response timing

# 🔌 API Endpoints

### `POST /ask`

Send a question and get a response from the LLM.

```json
{
  "query": "What is the average lead time for bookings?"
}
```

---

### `GET /`

Health check route — returns confirmation the app is running.

---

## 🧪 Sample Test Queries

- "What is the average lead time?"
- "Which hotel type has more bookings?"
- "What is the cancellation rate?"
- "Which month had the most bookings?"
- "How many bookings were made by families with children?"

---

## ⚡ Performance

- Average API response time: ~1.8 seconds
- Q&A accuracy: ✅ Matches expected values in all sample tests
