from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# First, create the FastAPI app instance
app = FastAPI()

# Then, add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Use ["http://localhost:3000"] if you want to restrict
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Then define your routes
@app.post("/ask")
async def ask_query(query: dict):
    # your logic here
    return {"response": f"Received query: {query['query']}"}
