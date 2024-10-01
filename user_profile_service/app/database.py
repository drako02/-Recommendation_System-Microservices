from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base, DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from typing import Type
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, future=True)

SessionLocal = sessionmaker(bind=engine,autoflush=False, expire_on_commit=False)

Base:Type[DeclarativeMeta] = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()