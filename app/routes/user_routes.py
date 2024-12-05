from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import schemas, database
from app.auth.dependencies import get_current_user
from app.db.crud import users

router = APIRouter()

@router.get("/me")
def get_me(current_user: dict = Depends(get_current_user)):
    return current_user

@router.get("/")
def get_users(db: Session = Depends(database.get_session_local)):
    return users.get_all_users(db)


@router.delete("/{user_id}")
def soft_delete_user(user_id: int, db: Session = Depends(database.get_session_local)):
    success = users.soft_delete_user(db, user_id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found or already deleted")
    return {"message": "User deleted successfully"}
