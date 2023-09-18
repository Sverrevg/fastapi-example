from pydantic import BaseModel


class ItemBase(BaseModel):  # type: ignore
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class UserBase(BaseModel):  # type: ignore
    email: str
    password: str
