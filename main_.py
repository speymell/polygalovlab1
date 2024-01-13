from fastapi import FastAPI, Response, Path, Body, Header
from fastapi.responses import PlainTextResponse
from Public.users import users_router
from datetime import datetime
from Public.router_users import init_db
from Public.router_users import users_router
app = FastAPI()

app.include_router(users_router)

@app.on_event("startup")
def on_startup():
    open("log.txt", mode="a").write(f'{datetime.utcnow()}: Begin\n')
    init_db()

@app.on_event("shutdown")
def shutdown():
    open("log.txt", mode="a").write(f'{datetime.utcnow()}: End\n')

#@app.get('/', response_class=PlainTextResponse)
#def f_indexH():
#    return "<b> Привет, пользователь!</b>"