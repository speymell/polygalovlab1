from fastapi import FastAPI, Response, Path, Body, Header
from fastapi.responses import PlainTextResponse
from Public.users import users_router
app = FastAPI()

app.include_router(users_router)

@app.get('/', response_class=PlainTextResponse)
def f_indexH():
    return "<b> Привет, пользователь!</b>"