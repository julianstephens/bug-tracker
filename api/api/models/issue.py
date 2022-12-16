import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship

from api.models import project
from .base import Base


class IssueStatus(str, enum.Enum):
    BACKLOG = ("backlog",)
    OPEN = ("open",)
    IN_PROGRESS = ("in progress",)
    UNDER_REVIEW = ("under review",)
    COMPLETED = "completed"


class IssuePriority(enum.Enum):
    HIGH = (1,)
    MEDIUM = (2,)
    LOW = (3,)


class Issue(Base):
    __tablename__ = "issues"

    project_id = Column(Integer, ForeignKey("projects.id"), nullable=False)
    title = Column(String, index=True, nullable=False)
    description = Column(String)
    status = Column(Enum(IssueStatus))
    label = Column(String)
    priority = Column(Enum(IssuePriority))

    project = relationship("Project", back_populates="issues")
    comments = relationship("Comment", back_populates="issue")
