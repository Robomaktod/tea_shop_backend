from sqlalchemy.orm import Session
from app.db import models, schemas

def create_review(db: Session, review: schemas.Review) -> models.Review:
    db_review = models.Review(
        user_id=review.user_id,
        tea_id=review.tea_id,
        content=review.content,
        rating=review.rating
    )
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def get_all_reviews(db: Session) -> list[models.Review]:
    return db.query(models.Review).all()

def get_review_by_id(db: Session, review_id: int) -> models.Review | None:
    return db.query(models.Review).filter(models.Review.id == review_id).first()

def update_review(db: Session, review_id: int, review_data: schemas.Review) -> models.Review | None:
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if review:
        review.content = review_data.content
        review.rating = review_data.rating
        db.commit()
        db.refresh(review)
    return review

def delete_review(db: Session, review_id: int) -> bool:
    review = db.query(models.Review).filter(models.Review.id == review_id).first()
    if review:
        db.delete(review)
        db.commit()
        return True
    return False
