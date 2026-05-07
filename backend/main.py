from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "NRSC RAG System Backend Running"}

@app.post("/chat")
def chat(request: ChatRequest):

    response = ollama.chat(
        model='phi3',
        messages=[
            {
                'role': 'user',
                'content': request.message
            }
        ]
    )

    return {
        "response": response['message']['content']
    }