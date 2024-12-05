from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import schemas, database
from app.auth.jwt_handler import create_access_token
from app.db.crud import users

router = APIRouter()

@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(database.get_session_local)):
    db_user = users.get_user_by_username(db, user.username)
    if not db_user or not users.pwd_context.verify(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    token = create_access_token(data={"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(database.get_session_local)):
    db_user = users.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    return users.create_user(db, user)
