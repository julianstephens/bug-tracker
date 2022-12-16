from typing import Any, List, Optional

from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import Issue, IssueCreate, IssueUpdate
from app.services import get_db

router = APIRouter()


@router.get("/", response_model=List[Issue])
def get_all_issues(
    db: AsyncSession = Depends(get_db), *, skip: int = 0, limit: int = 0
) -> Any:
    pass


@router.get("/{id}", response_model=Optional[Issue])
def get_issue(db: AsyncSession = Depends(get_db), *, id: int) -> Any:
    pass


@router.post("/", response_model=Issue)
def create_issue(db: AsyncSession = Depends(get_db), *, input: IssueCreate) -> Any:
    pass


@router.put("/{id}", response_model=Issue)
def update_issue(
    db: AsyncSession = Depends(get_db), *, id: int, input: IssueUpdate
) -> Any:
    pass


@router.delete("/{id}")
def delete_issue(db: AsyncSession = Depends(get_db), *, id: int) -> None:
    pass
