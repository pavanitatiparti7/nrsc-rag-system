from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.ollama_service import generate_response
from backend.rag.retriever import retrieve_relevant_chunks

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest):

    relevant_chunks = retrieve_relevant_chunks(request.message)

    context = "\n".join(relevant_chunks)

    response = generate_response(
        request.message,
        context
    )

    return {
        "response": response
    }