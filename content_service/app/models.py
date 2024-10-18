from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Movie model to store movie information
class Movie(Base):
    __tablename__ = "movies"
    
    movieId = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genres = Column(String)
    description = Column(Text)
    director = Column(String)
    release_year = Column(Integer)
    # Add more metadata as needed