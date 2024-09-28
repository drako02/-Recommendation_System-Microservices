from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    movie_data_path: str = '../data/movies.csv'

settings = Settings()