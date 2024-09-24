from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .models import Feedback
from .database import get_db

router = APIRouter()

# Submit feedback for a recommendation
@router.post("/feedback/{user_id}")
def submit_feedback(user_id: int, movie_id: int, rating: int, comment: str = None, db: Session = Depends(get_db)):
    feedback = Feedback(user_id=user_id, movie_id=movie_id, rating=rating, comment=comment)
    db.add(feedback)
    db.commit()
    return {"message": "Feedback submitted"}

# Fetch feedback history for a user
@router.get("/feedback/{user_id}/history")
def get_feedback_history(user_id: int, db: Session = Depends(get_db)):
    feedback_history = db.query(Feedback).filter(Feedback.user_id == user_id).all()
    return {"feedback_history": feedback_history}
