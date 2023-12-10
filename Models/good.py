from typing import Union, Annotated
from pydantic import BaseModel, Field, HttpUrl

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