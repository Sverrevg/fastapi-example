from typing import Any

from sqlalchemy.orm import Session

from src.database.models.models import Item
from src.database.schemas.schemas import ItemCreate


def get_items(session: Session, skip: int = 0, limit: int = 100) -> Any:
    return session.query(Item).offset(skip).limit(limit).all()


def create_user_item(session: Session, item: ItemCreate, user_id: int) -> Any:
    db_item = Item(**item.dict(), owner_id=user_id)
    session.add(db_item)
    session.commit()
    session.refresh(db_item)
    return db_item
