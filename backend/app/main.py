from fastapi import FastAPI

from backend.app.api.chat import router as chat_router
from backend.app.api.auth import router as auth_router
from backend.app.api.history import router as history_router

app = FastAPI(
    title="Customer Support AI"
)

app.include_router(chat_router)
app.include_router(auth_router)
app.include_router(history_router)


@app.get("/")
def home():
    return {
        "message": "Customer Support AI Backend Running"
    }