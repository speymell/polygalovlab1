import asyncio

from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine
ur_p = "postgresql+asyncpg://postgres:12345@localhost:5432/postgres"
engine = create_async_engine(ur_p, echo=True)

async def f():
    async with engine.begin() as conn:
        answer = conn.execute(text("select version()"))
        print(f"answer={answer}")
asyncio.get_event_loop().run_until_complete(f())