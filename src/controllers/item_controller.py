from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database.database_context import get_db
from src.database.schemas.schemas import ItemCreate
from src.services import item_service

router = APIRouter()


@router.post("/{user_id}/", response_model=None)
def create_item_for_user(user_id: int, item: ItemCreate, session: Session = Depends(get_db)) -> Any:
    return item_service.create_user_item(session=session, item=item, user_id=user_id)


@router.get("/", response_model=None)
def read_items(skip: int = 0, limit: int = 100, session: Session = Depends(get_db)) -> Any:
    items = item_service.get_items(session, skip=skip, limit=limit)
    return items
