from fastapi import FastAPI

from models.poll import Poll
from models.user import User

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/users/")
async def create_user(user: User):
    return user


@app.post("/polls/")
async def create_poll(poll: Poll):
    return poll
