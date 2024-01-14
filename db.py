import asyncio
#from config import settings
from Models.good import Base, User
from sqlalchemy import create_engine, text, insert, select
from sqlalchemy.ext.asyncio import create_async_engine
from config import  settings
#ur_p = "postgresql+asyncpg://postgres:12345@localhost:5432/postgres"
#engine = create_async_engine(ur_p, echo=True)
ur_s = "postgresql://postgres@localhost:5432/postgres"

print(ur_s)
engine_s = create_engine(ur_s, echo=True)
# async def f():
#     async with engine_a.connect() as conn:
#         answer = await conn.execute(text('select * from users;'))
#         print(f'answer={answer.all()}')
# asyncio.get_event_loop().run_until_complete(f())
# async def fa_bilder():
#     with engine_a.connect() as conn:
#         query = insert(User).values([
#             {"name": "Joe Biden", "hashed password": "12345", "email":"whitehome@yandex.ru"}
#         ])
def create_tables():
    Base.metadata.drop_all(bind=engine_s)
    Base.metadata.create_all(bind=engine_s)
def f():
    with engine_s.connect() as conn:
        answer = conn.execute(text('select * from users;'))
        print(f'answer={answer.all()}')
def f_bilder():
    with engine_s.connect() as conn:
        query = insert(User).values([
            {"name": "Joe Biden", "hashed password": "12345", "email":"whitehome@yandex.ru"}
        ])