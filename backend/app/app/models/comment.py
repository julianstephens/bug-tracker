from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Comment(Base):
    __tablename__ = "comments"

    issue_id = Column(Integer, ForeignKey("issues.id"))
    title = Column(String, nullable=True)
    body = Column(String)

    issue = relationship("Issue", back_populates="comments")
