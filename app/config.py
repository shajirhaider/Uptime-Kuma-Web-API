from pydantic import AnyHttpUrl, BaseSettings
from fastapi.logger import logger as fast_api_logger
from typing import List
import secrets
import logging
import os

logger = logging.getLogger("gunicorn.error")
fast_api_logger.handlers = logger.handlers


class Settings(BaseSettings):
    PROJECT_NAME: str = "Uptime-Kuma-API"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    ACCESS_TOKEN_EXPIRE: int = os.environ.get(
        "ACCESS_TOKEN_EXPIRATION", 60 * 24 * 8
    )  # 8 days
    SECRET_KEY: str = os.environ.get("SECRET_KEY", secrets.token_urlsafe(32))

    # KUMA_SERVER: str = os.environ.get("KUMA_SERVER")
    # KUMA_USERNAME: str = os.environ.get("KUMA_USERNAME")
    # KUMA_PASSWORD: str = os.environ.get("KUMA_PASSWORD")

    # ADMIN_PASSWORD: str = os.environ.get("ADMIN_PASSWORD")

    # SECRET_KEY: str = '6eea597b7f37f3804acdaf43d1ca663910'

    KUMA_SERVER: str = 'http:/127.0.0.1:3001'
    KUMA_USERNAME: str = 'admin'
    KUMA_PASSWORD: str = 'Test.1234'
    ADMIN_PASSWORD: str = 'Test.1234'
    # KUMA_SERVER: str = 'http://18.139.51.148:8000'
    # KUMA_USERNAME: str = 'admin'
    # KUMA_PASSWORD: str = 'Udaipur@97842!'
    # ADMIN_PASSWORD: str = 'Udaipur@97842!'
    class Config:
        case_sensitive = True
        # env_file = ".env"


settings = Settings()
