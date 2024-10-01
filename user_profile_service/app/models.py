from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base
from passlib.context import CryptContext


# Password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"])

# User model to store user information
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    preferences = Column(Text)  # Store movie genre preferences (e.g., "Action, Drama")
    history = relationship("InteractionHistory", back_populates="user")

    def set_password(self, password: str):
        self.password_hash = pwd_context(password)

    def verify_password(self, password: str) -> bool:
        return pwd_context.verify(password, self.password_hash)

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

