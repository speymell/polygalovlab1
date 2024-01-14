import asyncio
from config import settings
from Models.good import Base, User
from sqlalchemy import create_engine, text, insert, select
from sqlalchemy.ext.asyncio import create_async_engine
ur_p = "postgresql+asyncpg://postgres:12345@localhost:5432/postgres"
#engine = create_async_engine(ur_p, echo=True)
ur_a = settings.POSTGRES_DATABASE_URL

print(ur_a)
engine_a = create_async_engine(ur_a, echo=True)
#async def f():
#    async with engine.begin() as conn:
#        answer = conn.execute(text("select version()"))
#        print(f"answer={answer}")
#asyncio.get_event_loop().run_until_complete(f())
def create_tables():
    Base.metadata.drop_all(bind=engine_a)
    Base.metadata.create_all(bind=engine_a)
def f():