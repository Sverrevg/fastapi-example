from typing import Any

from sqlalchemy.orm import Session

from src.database.models.models import User
from src.database.schemas.schemas import UserBase


def get_user(session: Session, user_id: int) -> Any:
    return session.query(User).filter(User.id == user_id).first()


def get_user_by_email(session: Session, email: str) -> Any:
    query = session.query(User).filter(User.email == email).first()
    return query


def get_users(session: Session, skip: int = 0, limit: int = 100) -> Any:
    return session.query(User).offset(skip).limit(limit).all()


def create_user(session: Session, user: UserBase) -> Any:
    fake_hashed_password = user.password + "notreallyhashed"
    session_user = User(email=user.email, hashed_password=fake_hashed_password)
    session.add(session_user)
    session.commit()
    session.refresh(session_user)
    return session_user
