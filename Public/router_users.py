from sqlalchemy import create_engine
from fastapi import APIRouter, Body, status, HTTPException, Depends
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from Models.good import User, Base, Tags , Main_User, New_Respons
#from config import settings
from typing import Union, Annotated

engine = create_engine("postgresql://postgres:12345@localhost:5432/postgres", connect_args={"check_same_thread": True})

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

@users_router.get("/{id}",response_model=Union[New_Respons, Main_User], tags=[Tags.info])
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
# @users_router.post("/", response_model=Union[Main_User, New_Respons], tags=[Tags.users], status_code=status.HTTP_201_CREATED)
# def create_user(item: Annotated[Main_User, Body(embed=True, description="Новый пользователь")], DB: Session = Depends((get_session()))):
#     try:
#         user = User(id=item.id, name=item.name, hashed_password=coder_passwd(item.name))
#
#         if user is None:
#             raise HTTPException(status_code=404, detail="Объект не определён!")
#         DB.add(user)
#         DB.commit()
#         DB.refresh()
#         return user
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Произошла ошибка при добавлении объекта{user}")
@users_router.put("/", response_model=Union[Main_User, New_Respons], tags=[Tags.users])

@users_router.patch("/{id}", response_model=Union[Main_User, New_Respons], tags=[Tags.users])
#def edit_user(item: Annotated[Main_User, Body(embed=True)]):
@users_router.delete("/{id}", response_class=JSONResponse, tags=[Tags.users])
def delete_user(id: int, DB: Session = Depends(get_session)):
    user = DB.query(User).filter(User.id == id).first()
    if user == None:
        return JSONResponse(status_code=404, content={"message": "Пользователь не найден"})
    try:
        DB.delete(user)
        DB.commit()  # сохраняем изменения
    except HTTPException:
        JSONResponse(content={'message': f'Ошибка'})
    return JSONResponse(content={'message': f'Пользователь удалён {id}'})
# @users_router.patch("/{id}", response_model=Union[Main_User, New_Respons], tags=[Tags.users])
# def edit_user(item: Annotated[Main_User, Body(embed=True, description="Изменяем данные по id")], DB: Session = Depends(get_session)):
#     try:
#         item_good = find_good(str(item.id))
#         item_good = good_dict[str(item.id)]
#         if item_good == None:
#         return New_Respons(message="ошибка")
#         good_model = Good(**item_good)   #преобразовали элемент из словаря в модель
#         update_good_dict = item.dict(exclude_unset=True) #преобразуем объект модели в словарь, но только только те данные,
#             # которые были установлены (отправлены в запросе), без значений по умолчанию (данные для изменения в удобный
#     #         # формат)
#         good_model_copy = good_model.copy(update=update_good_dict) # обновляем данные  модели на новые
#         good_dict[str(item.id)] = jsonable_encoder(good_model_copy)
#         return good_model_copy
#     except HTTPException:
#         return New_Respons(message = f'Ошибка {response.status_code}')
