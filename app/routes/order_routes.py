from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import schemas, database
from app.db.crud import orders as order_crud

router = APIRouter()

@router.get("/")
def get_orders(db: Session = Depends(database.get_session_local)):
    return order_crud.get_all_orders(db)

@router.post("/")
def create_order(order: schemas.Order, db: Session = Depends(database.get_session_local)):
    return order_crud.create_order(db, order)

@router.get("/{order_id}")
def get_order(order_id: int, db: Session = Depends(database.get_session_local)):
    order = order_crud.get_order_by_id(db, order_id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@router.delete("/{order_id}")
def delete_order(order_id: int, db: Session = Depends(database.get_session_local)):
    success = order_crud.delete_order(db, order_id)
    if not success:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"message": "Order deleted successfully"}
