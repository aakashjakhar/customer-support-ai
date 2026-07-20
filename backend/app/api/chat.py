from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.database import SessionLocal
from backend.app.database.schemas import ChatRequest
from backend.app.database.models import ChatHistory

from backend.app.agents.intent_detector import detect_intent
from backend.app.agents.router import route_intent
from backend.app.memory.memory_manager import memory

router = APIRouter()


# Database Connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/chat")
def chat(request: ChatRequest, db: Session = Depends(get_db)):

    # Save User Message in Memory
    memory.add_user_message(request.message)

    # Detect Intent
    intent = detect_intent(request.message)

    # Get AI Response
    ai_response = route_intent(intent, request.message)

    # Save AI Response in Memory
    memory.add_ai_message(ai_response)

    # Save Chat History in MySQL
    chat = ChatHistory(
        user_id=request.user_id,
        question=request.message,
        answer=ai_response
    )

    db.add(chat)
    db.commit()

    return {
        "user_id": request.user_id,
        "user_message": request.message,
        "intent": intent,
        "ai_response": ai_response
    }