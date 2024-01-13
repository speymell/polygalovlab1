from sqlalchemy import create_engine
from fastapi import APIRouter, Body, status, HTTPException, Depends
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from Models.good import Base, Tags #здесь дальше ещё что-то импортировать
from config import settings
from typing import Union, Annotated

engine = create_engine(settings.POSTGRES_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def init_db():
    Base.metadata.create_all(bind=engine)

def get_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()

users_router = APIRouter(tags=[Tags.users], prefix='/api/users')
info_router = APIRouter(tags=[Tags.info])