import enum

from pydantic import BaseModel


class IssueBase(BaseModel):
    title: str
    description: str
    status: enum.Enum
    label: str
    priority: enum.Enum


class Issue(IssueBase):
    id: int

    class Config:
        orm_mode = True
