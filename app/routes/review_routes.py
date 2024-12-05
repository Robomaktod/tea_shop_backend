from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import schemas, database
from app.db.crud import reviews as review_crud

router = APIRouter()

@router.post("/")
def create_review(review: schemas.Review, db: Session = Depends(database.get_session_local)):
    return review_crud.create_review(db, review)

@router.get("/")
def get_reviews(db: Session = Depends(database.get_session_local)):
    return review_crud.get_all_reviews(db)

@router.get("/{review_id}")
def get_review(review_id: int, db: Session = Depends(database.get_session_local)):
    review = review_crud.get_review_by_id(db, review_id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@router.put("/{review_id}")
def update_review(review_id: int, review_data: schemas.ReviewUpdate, db: Session = Depends(database.get_session_local)):
    review = review_crud.update_review(db, review_id, review_data)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@router.delete("/{review_id}")
def delete_review(review_id: int, db: Session = Depends(database.get_session_local)):
    success = review_crud.delete_review(db, review_id)
    if not success:
        raise HTTPException(status_code=404, detail="Review not found")
    return {"message": "Review deleted successfully"}
