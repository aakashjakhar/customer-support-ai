from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.app.database.database import SessionLocal
from backend.app.database.models import User
from backend.app.database.schemas import UserRegister, UserLogin

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ==========================
# Register API
# ==========================
@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists."
        )

    new_user = User(
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "message": "Registration Successful"
    }


# ==========================
# Login API
# ==========================
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        User.email == user.email,
        User.password == user.password
    ).first()

    if not existing_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Email or Password"
        )

    return {
        "message": "Login Successful",
        "user_id": existing_user.id,
        "username": existing_user.username,
        "email": existing_user.email
    }