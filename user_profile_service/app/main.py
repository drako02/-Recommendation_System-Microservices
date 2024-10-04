from fastapi import FastAPI
from .routes import router as user_router
from .database import Base, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Or "*" to allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(user_router)

