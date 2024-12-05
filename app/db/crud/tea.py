from sqlalchemy.orm import Session
from app.db import models, schemas

def create_tea(db: Session, tea: schemas.Tea) -> models.Tea:
    """
    Create a new tea record.
    """
    db_tea = models.Tea(name=tea.name, description=tea.description, price=tea.price)
    db.add(db_tea)
    db.commit()
    db.refresh(db_tea)
    return db_tea

def get_all_teas(db: Session) -> list[models.Tea]:
    """
    Get all teas.
    """
    return db.query(models.Tea).all()

def get_tea_by_id(db: Session, tea_id: int) -> models.Tea | None:
    """
    Retrieve a tea by ID.
    """
    return db.query(models.Tea).filter(models.Tea.id == tea_id).first()

def delete_tea(db: Session, tea_id: int) -> bool:
    """
    Delete a tea by ID.
    """
    tea = db.query(models.Tea).filter(models.Tea.id == tea_id).first()
    if tea:
        db.delete(tea)
        db.commit()
        return True
    return False
