from sqlalchemy.orm import relationship
from .base import Base
from sqlalchemy import Column, String


class User(Base):
    __tablename__ = "users"

    fname = Column(String, index=True, nullable=False)
    lname = Column(String, index=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    passwordHash = Column(String, nullable=False)

    projects = relationship("Project", back_populates="user")
