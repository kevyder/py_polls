from typing import List

from fastapi import Depends, FastAPI, HTTPException

import crud
import models
import schemas
from database import Session, engine

models.Base.metadata.create_all(engine)

app = FastAPI()


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


@app.get("/users/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db=db, user_id=user_id)
    return user


@app.get("/users/", response_model=List[schemas.User])
def get_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = crud.get_users(db=db, skip=skip, limit=limit)
    return users


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/polls/", response_model=List[schemas.Poll])
def get_polls(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    polls = crud.get_polls(db=db, skip=skip, limit=limit)
    return polls


@app.post("/polls/")
async def create_poll(poll: schemas.PollBase, db: Session = Depends(get_db)):
    return crud.create_poll(db=db, poll=poll)
