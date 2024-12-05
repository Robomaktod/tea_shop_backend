from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import schemas, database
from app.db.crud import tea as tea_crud

router = APIRouter()

@router.get("/")
def get_teas(db: Session = Depends(database.get_session_local)):
    return tea_crud.get_all_teas(db)

@router.post("/")
def create_tea(tea: schemas.Tea, db: Session = Depends(database.get_session_local)):
    db_tea = tea_crud.create_tea(db, tea)
    return db_tea

@router.get("/{tea_id}")
def get_tea(tea_id: int, db: Session = Depends(database.get_session_local)):
    tea = tea_crud.get_tea_by_id(db, tea_id)
    if not tea:
        raise HTTPException(status_code=404, detail="Tea not found")
    return tea

@router.delete("/{tea_id}")
def delete_tea(tea_id: int, db: Session = Depends(database.get_session_local)):
    success = tea_crud.delete_tea(db, tea_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tea not found")
    return {"message": "Tea deleted successfully"}
