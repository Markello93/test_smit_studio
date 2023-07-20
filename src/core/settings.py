from functools import cache

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Настройки проекта."""

    DEBUG: bool = False
    CARGO_ROOT_PATH: str = ""
    CARGO_APP_DB_NAME: str
    CARGO_APP_DB_USER: str
    CARGO_APP_DB_PASSWORD: str
    DB_HOST: str
    DB_PORT: int
    APPS_MODELS: str = "src.db.models"

    @property
    def database_url(self) -> str:
        """Получить ссылку для подключения к DB."""
        return (
            f"postgres://{self.CARGO_APP_DB_USER}:{self.CARGO_APP_DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.CARGO_APP_DB_NAME}"
        )

    class Config:
        env_file = ".env"


@cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
