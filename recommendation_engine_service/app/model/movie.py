from pydantic import BaseModel
from typing import List

class Movie(BaseModel):
    movie_id: int
    title: str
    genres:List[str]
    

