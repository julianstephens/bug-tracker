from typing import Any, List, Optional

from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import Project, ProjectCreate, ProjectUpdate
from app.services import get_db

router = APIRouter()


@router.get("/", response_model=List[Project])
def get_all_projects(
    db: AsyncSession = Depends(get_db), *, skip: int = 0, limit: int = 0
) -> Any:
    pass


@router.get("/{id}", response_model=Optional[Project])
def get_project(db: AsyncSession = Depends(get_db), *, id: int) -> Any:
    pass


@router.post("/", response_model=Project)
def create_project(db: AsyncSession = Depends(get_db), *, input: ProjectCreate) -> Any:
    pass


@router.put("/{id}", response_model=Project)
def update_project(
    db: AsyncSession = Depends(get_db), *, id: int, input: ProjectUpdate
) -> Any:
    pass


@router.delete("/{id}")
def delete_project(db: AsyncSession = Depends(get_db), *, id: int) -> None:
    pass
