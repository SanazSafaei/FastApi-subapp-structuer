# custom config base projects.

from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv(verbose=True)


class Settings(BaseSettings):
    SECRET_KEY: str
    ALLOWED_HOSTS: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    DEBUG: int

    # databases
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
