from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.crud.user import get_user_by_email, create_user
from app.schemas.user import UserCreate

def register_user_service(db: Session, user: UserCreate):
    existing = get_user_by_email(db, user.email)

    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    return create_user(db, user)