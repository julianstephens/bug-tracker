from typing import Any, List, Optional

from fastapi import APIRouter
from fastapi.param_functions import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas import Comment, CommentCreate, CommentUpdate
from app.services import get_db

router = APIRouter()


@router.get("/", response_model=List[Comment])
def get_all_comments(
    db: AsyncSession = Depends(get_db), *, skip: int = 0, limit: int = 0
) -> Any:
    pass


@router.get("/{id}", response_model=Optional[Comment])
def get_comment(db: AsyncSession = Depends(get_db), *, id: int) -> Any:
    pass


@router.post("/", response_model=Comment)
def create_comment(db: AsyncSession = Depends(get_db), *, input: CommentCreate) -> Any:
    pass


@router.put("/{id}", response_model=Comment)
def update_comment(
    db: AsyncSession = Depends(get_db), *, id: int, input: CommentUpdate
) -> Any:
    pass


@router.delete("/{id}")
def delete_comment(db: AsyncSession = Depends(get_db), *, id: int) -> None:
    pass
