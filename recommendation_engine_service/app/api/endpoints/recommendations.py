from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from app.core.recommendation import get_similar_movies
from app.data.data_loader import load_movie_data
import pandas as pd
import pprint

router = APIRouter()

# Load the data
# movies: pd.DataFrame

movies , genre_matrix = load_movie_data()



@router.get("/recommend/{movie_id}")
def recommend(movie_id: int, top_n: int = 10):
    if movie_id not in movies['movieId'].values:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    similar_movies_ids = get_similar_movies(movie_id, genre_matrix, top_n)
    recommended_movies = movies[movies['movieId'].isin(similar_movies_ids)][['movieId', 'title', 'genres']]

    result = recommended_movies.to_dict(orient='records')
    pprint.pprint(JSONResponse(content=result))
    return JSONResponse(content=result)
    
