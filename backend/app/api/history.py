from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app.database.database import SessionLocal
from backend.app.database.models import ChatHistory

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/chat-history/{user_id}")
def get_chat_history(user_id: int, db: Session = Depends(get_db)):

    chats = db.query(ChatHistory).filter(
        ChatHistory.user_id == user_id
    ).all()

    history = []

    for chat in chats:
        history.append({
            "question": chat.question,
            "answer": chat.answer
        })

    return {
        "user_id": user_id,
        "history": history
    }