from sqlalchemy.orm import Session
from app.db import models, schemas

def get_all_orders(db: Session) -> list[models.Order]:
    return db.query(models.Order).all()

def get_order_by_id(db: Session, order_id: int) -> models.Order | None:
    return db.query(models.Order).filter(models.Order.id == order_id).first()

def create_order(db: Session, order: schemas.Order) -> models.Order:
    db_order = models.Order(
        user_id=order.user_id,
        tea_id=order.tea_id,
        quantity=order.quantity
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def delete_order(db: Session, order_id: int) -> bool:
    order = db.query(models.Order).filter(models.Order.id == order_id).first()
    if order:
        db.delete(order)
        db.commit()
        return True
    return False
