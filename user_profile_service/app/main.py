from fastapi import FastAPI
from .routes import router as user_router
from .database import Base, engine

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(user_router)

