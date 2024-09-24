from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .models import User, InteractionHistory, Movie
from .database import get_db

router = APIRouter()

# Fetch movie metadata
@router.get("/movie/{movie_id}")
def get_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

# For testing purposes -- Add  amovie to the database
class MovieCreate(BaseModel):
    title: str
    genre: str
    description: str
    director: str
    release_year: int

@router.post("/movie/")
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    new_movie = Movie(
        title=movie.title,
        genre=movie.genre,
        description=movie.description,
        director=movie.director,
        release_year=movie.release_year
    )
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    return {"message": "Movie added", "movie": new_movie}