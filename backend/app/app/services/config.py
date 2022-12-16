import os
from app.decorators import singleton
from pydantic import BaseSettings


@singleton
class Settings(BaseSettings):
    DB_URI: str
    AUTH0_DOMAIN: str
    AUTH0_AUDIENCE: str
    AUTH0_ALGORITHMS: str
    AUTH0_ISSUER: str

    class Config:
        env_file = os.path.join(os.path.dirname(__file__), "../../.env")
        case_sensitive = True


settings = Settings().dict()  # type: ignore
