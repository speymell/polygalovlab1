from dotenv import load_dotenv
import os
class Settings:
    app_name: str = "NEW API"
    admin_email: str = "stasl22@mail.ru"
    POSTGRES_DATABASE_URLS: str = "postgresql://postgres:12345@localhost:5432/postgres"
    POSTGRES_DATABASE_URLA: str = "postgresql+asyncpg://postgres:12345@localhost:5432/postgres"
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_HOST: str

load_dotenv()
settings = Settings()
settings.POSTGRES_PORT = os.environ.get('POSTGRES_PORT')
settings.POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
settings.POSTGRES_USER = os.environ.get('POSTGRES_USER')
settings.POSTGRES_DB = os.environ.get('POSTGRES_DB')
settings.POSTGRES_HOST = os.environ.get('POSTGRES_HOST')

settings.POSTGRES_DATABASE_URLS = f"postgresql:" \
                                 f"//{settings.POSTGRES_USER}:" \
                                 f"{settings.POSTGRES_PASSWORD}" \
                                 f"@{settings.POSTGRES_HOST}:" \
                                 f"{settings.POSTGRES_PORT}" \
                                 f"/{settings.POSTGRES_DB}"
settings.POSTGRES_DATABASE_URLA = f"postgresql+asyncpg:" \
                                 f"//{settings.POSTGRES_USER}:" \
                                 f"{settings.POSTGRES_PASSWORD}" \
                                 f"@{settings.POSTGRES_HOST}:" \
                                 f"{settings.POSTGRES_PORT}" \
                                 f"/{settings.POSTGRES_DB}"