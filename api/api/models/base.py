from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column

_Base = declarative_base()

class Base(_Base):
    id = Column(Integer, primary_key=True, index=True)

    __abstract__ = True
    __name__: str

    def __repr__(self) -> str:
        columns = ", ".join([f"{k}={repr(v)}" for k,v in self.__dict__.items() if not k.startswith("_")])
        return f"<{self.__class__.__name__}({columns})>"
    
