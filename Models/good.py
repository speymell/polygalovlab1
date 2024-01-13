from typing import Union, Annotated, List, Optional
from pydantic import BaseModel, Field, HttpUrl
from sqlalchemy import Column, Integer, Float, Sequence , Boolean, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base
from enum import Enum
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence("user_id_seq", start=1), primary_key = True)
    name = Column(String,index=True,nullable=False)
    hashed_password = Column(String)

    #goods = relationship("Good", back_populates="owner")
    #class Good(metadata):
    #__tablename__ = "goods"
    #id = Column(Integer, primary_key=True, index=True)
    #name = Column(String, index=True)
    #description = Column(String, index=True)
    #price = Column(Float)
    #nalog = Column(Float)
    #user_id = Column(Integer, ForeignKey("users.id"))
    #owner = relationship("User", back_populates=goods)

class Person(BaseModel):
    lastName: str = Field(default="lastName", min_length=3, max_length=35)
    age: int = Field(default=100, ge=10, lt=200)

class Foto(BaseModel):
    url:HttpUrl
    name:Union[str,None] = None

class User(BaseModel):
    name: Union[str, None] = None
    id: Annotated[Union[int,None], Field(default=100,ge=10,lt=200)] = None
    person: Union[Person, None] = None
    day_list0 : list
    day_list1: Union[list, None] = None

class Main_User(BaseModel):
    name: Union[str, None] = None
    id: Annotated[Union[int,None], Field(default=100, ge=1, lt=200)] = None

class Main_UserDB(Main_User):
    password: Annotated[Union[str, None], Field(max_length=200,min_length=8)] = None

class New_Respons(BaseModel):
    message: str