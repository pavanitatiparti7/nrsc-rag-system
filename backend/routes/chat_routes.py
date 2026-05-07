from fastapi import APIRouter
from pydantic import BaseModel

from backend.services.ollama_service import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest):

    response = generate_response(request.message)

    return {
        "response": response
    }