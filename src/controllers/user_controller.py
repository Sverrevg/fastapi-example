from typing import Any

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session
from starlette import status

from src.database.database_context import get_db
from src.database.schemas.schemas import UserBase
from src.services import user_service
from src.services.user_service import get_user_by_email

router = APIRouter()


@router.post("/", response_model=None, status_code=status.HTTP_201_CREATED)
def create_user(user: UserBase, session: Session = Depends(get_db)) -> Any:
    db_user = get_user_by_email(session, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return user_service.create_user(session=session, user=user)


@router.get("/", response_model=None)
def read_users(skip: int = 0, limit: int = 100, session: Session = Depends(get_db)) -> Any:
    return user_service.get_users(session, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=None)
def read_user(user_id: int, session: Session = Depends(get_db)) -> Any:
    db_user = user_service.get_user(session, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
