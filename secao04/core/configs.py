from typing import Any

from pydantic_settings import BaseSettings
from sqlalchemy.orm import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """

    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:postgresdev@localhost:5432/faculdade"
    DBBaseModel: Any = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
