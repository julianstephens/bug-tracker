from pydantic import BaseModel


class CommentBase(BaseModel):
    title: str
    body: str


class Comment(CommentBase):
    id: int

    class Config:
        orm_mode = True
