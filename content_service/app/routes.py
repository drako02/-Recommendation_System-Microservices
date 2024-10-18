from fastapi import APIRouter, Depends, HTTPException
from fastapi.params import Query
from pydantic import BaseModel
from sqlalchemy.orm import Session
from .models import  Movie
from .database import get_db
from typing import List

router = APIRouter()

class Movie_Data(BaseModel):
    movieId:int
    title:str
    genres:str

    class Config:
        orm_mode = True

class MovieResponse(BaseModel):
    movies: List[Movie_Data]

# Fetch movie metadata
@router.get("/movies/", response_model=MovieResponse)
def get_movie(
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    movies = db.query(Movie).offset(offset).limit(limit).all()
    return {"movies": movies} 


# class MovieCreate(BaseModel):
#     title:str
#     genre: str
#     description:str

# @router.post("/movie")
# def create_movie(movie: MovieCreate, db:Session = De[])
# For testing purposes -- Add  amovie to the database
# class MovieCreate(BaseModel):
#     title: str
#     genre: str
#     description: str
#     director: str
#     release_year: int

# @router.post("/movie/")
# def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
#     new_movie = Movie(
#         title=movie.title,
#         genre=movie.genre,
#         description=movie.description,
#         director=movie.director,
#         release_year=movie.release_year
#     )
#     db.add(new_movie)
#     db.commit()
#     db.refresh(new_movie)
#     return {"message": "Movie added", "movie": new_movie}