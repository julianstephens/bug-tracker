from pydantic import BaseModel


class UserBase(BaseModel):
    fname: str
    lname: str
    email: str
    passwordHash: str


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
