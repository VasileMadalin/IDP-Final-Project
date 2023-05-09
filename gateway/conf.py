import os

from pydantic import BaseSettings


class Settings(BaseSettings):
    COMMENTS_SERVICE_URL: str = os.environ.get('COMMENTS_SERVICE_URL')
    TWEETS_SERVICE_URL: str = os.environ.get('TWEETS_SERVICE_URL')
    AUTH_SERVICE_URL: str = os.environ.get('AUTH_SERVICE_URL')
    GATEWAY_TIMEOUT: int = 59

settings = Settings()
