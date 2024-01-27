import uvicorn
from fastapi import FastAPI, Response, Path, Body, Header, Body, status, HTTPException, Depends
#from Public.users import users_router
from Public.router_users import users_router
from db import *
import requests
from bs4 import BeautifulSoup

response = requests.get('https://2ip.ru/')
soup = BeautifulSoup(response.content, 'htmp.parser')

my_ip = soup.find('div', class_='ip')
print(my_ip.text)

app = FastAPI()
#f_builder()
#fa()
f()
app.include_router(users_router)

#@app.get('/')
#def main():
#    return FileResponse("files/index.html")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)