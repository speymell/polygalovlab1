from dotenv import load_dotenv
import os

class Settings:
    app_name: str = "New API"
    admin_email: str = "nicegeaming@yandex.ru"
    POSTGRES_DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/db"
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    POSTGRES_DB: str

load_dotenv()
settings = Settings()

settings.POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
settings.POSTGRES_PASSWORD = os.environ.get('POSTGRES_PORT')
settings.POSTGRES_USER = os.environ.get('POSTGRES_PORT')
settings.POSTGRES_DB = os.environ.get('POSTGRES_PORT')
settings.POSTGRES_DATABASE_URL = f"postgresql+asyncpg:" \
                                f"//{settings.POSTGRES_USER}:" \
                                f"{settings.POSTGRES_PASSWORD}" \
                                f"@{settings.POSTGRES_HOST}:" \
                                f"{settings.POSTGRES_PORT}" \
                                f"/{settings.POSTGRES_DB}"