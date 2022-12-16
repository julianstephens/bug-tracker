from fastapi import APIRouter
from .endpoints import issues, projects, comments

api_router = APIRouter()
api_router.include_router(projects.router, prefix="/projects", tags=["projects"])
api_router.include_router(issues.router, prefix="/issues", tags=["issues"])
api_router.include_router(comments.router, prefix="/comments", tags=["comments"])
