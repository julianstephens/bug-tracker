import enum
from typing import Optional

from pydantic import BaseModel


class IssueBase(BaseModel):
    title: str
    description: str
    status: enum.Enum
    label: str
    priority: enum.Enum


class IssueCreate(IssueBase):
    pass


class IssueUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[enum.Enum] = None
    label: Optional[str] = None
    priority: Optional[enum.Enum] = None


class Issue(IssueBase):
    id: int

    class Config:
        orm_mode = True
