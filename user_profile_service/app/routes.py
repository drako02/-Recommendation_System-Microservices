from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .models import User, InteractionHistory, Movie
from .database import get_db

router = APIRouter()

# Fetch user preferences
@router.get("/user/{user_id}/preferences")
def get_user_preferences(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return {"preferences": user.preferences}

# Update user preferences
@router.post("/user/{user_id}/update_preferences")
def update_user_preferences(user_id: int, preferences: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.preferences = preferences
    db.commit()
    db.refresh(user)
    return {"message": "Preferences updated", "user": user}

# Fetch movie metadata
# @router.get("/movie/{movie_id}")
# def get_movie(movie_id: int, db: Session = Depends(get_db)):
#     movie = db.query(Movie).filter(Movie.id == movie_id).first()
#     if movie is None:
#         raise HTTPException(status_code=404, detail="Movie not found")
#     return movie

# Fetch user interaction history
@router.get("/user/{user_id}/history")
def get_user_history(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    history = db.query(InteractionHistory).filter(InteractionHistory.user_id == user_id).all()
    return {"history": history}

# Add user interaction with a movie (e.g., watched, liked)
@router.post("/user/{user_id}/add_history")
def add_user_history(user_id: int, movie_id: int, interaction_type: str, rating: int = None, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    
    if user is None or movie is None:
        raise HTTPException(status_code=404, detail="User or Movie not found")
    
    new_history = InteractionHistory(movie_id=movie_id, interaction_type=interaction_type, user_id=user_id, rating=rating)
    db.add(new_history)
    db.commit()
    db.refresh(new_history)
    return {"message": "History added", "history": new_history}


class UserCreate(BaseModel):
    name: str
    email: str  
    password: str

router.post("/register")
def register_user(user:UserCreate, db: Session = Depends(get_db) ):
    existing_user = db.query(User).filter((User.name == user.name) | (User.email == user.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")
    
    # Create new user
    new_user = User(name = user.name, email = user.email )
    new_user.set_password(user.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created", "user": new_user}

class UserLogin(BaseModel):
    name_or_email: str
    password: str

router.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter((User.name == user.name_or_email) | (User.email == user.name_or_email)).first()

    # Verify the password
    if not existing_user or not existing_user.verify_password(user.password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    return {"message": "Login successful", "user_id": existing_user.id}

