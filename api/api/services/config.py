import os
from api.decorators import singleton
from pydantic import BaseSettings


@singleton
class Settings(BaseSettings):
    DB_URI: str

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "../../.env")
        case_sensitive = True

settings = Settings().dict() # type: ignore
