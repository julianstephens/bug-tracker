from typing import Optional
from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str
    description: str


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True
