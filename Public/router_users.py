from sqlalchemy import create_engine
from fastapi import APIRouter, Body, status, HTTPException, Depends
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from Models.good import Base, Tags, User, New_Respons, Main_User #эти слова, начиная с тэг необходимо дописать в модели
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

def coder_passwd(cod:str):
    return cod*2

@users_router.get("/{id}",response_model=Union[New_Respons, Main_User], tags=[Tags.Info])
def get_user_(id:int,response: Response, DB: Session = Depends(get_session)):
    '''
    po id
    '''
    user = DB.query(User).filter(User.id==id).first()
    if user == None:
        return JSONResponse(status_code=404, content={'message': "Пользователь не найден!"})
    else:
        return user
#@users_router.get("/",response_model=Union[list[Main_User], New_Respons, tags=[Tags.users])