from typing import Optional
from pydantic import BaseModel


class CommentBase(BaseModel):
    title: str
    body: str


class CommentCreate(CommentBase):
    pass


class CommentUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None


class Comment(CommentBase):
    id: int

    class Config:
        orm_mode = True
