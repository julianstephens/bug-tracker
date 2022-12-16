from pydantic import BaseModel


class ProjectBase(BaseModel):
    name: str
    description: str


class Project(ProjectBase):
    id: int

    class Config:
        orm_mode = True
