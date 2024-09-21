from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# User model to store user information
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    preferences = Column(Text)  # Store movie genre preferences (e.g., "Action, Drama")
    history = relationship("InteractionHistory", back_populates="user")

# Movie model to store movie information
class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String)
    description = Column(Text)
    director = Column(String)
    release_year = Column(Integer)
    # Add more metadata as needed

# Interaction history model for tracking user interactions with movies
class InteractionHistory(Base):
    __tablename__ = "interaction_history"
    
    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, ForeignKey('movies.id'))  # Link to Movie model
    interaction_type = Column(String)  # e.g., "viewed", "liked", "rated"
    rating = Column(Integer, nullable=True)  # Optional rating (1-5 stars)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    # Relationships
    user = relationship("User", back_populates="history")
    movie = relationship("Movie")
