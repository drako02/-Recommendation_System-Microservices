# from contextlib import asynccontextmanager
import os
from fastapi import Depends, FastAPI
# from sqlalchemy import insert

# from app.models import Movie
from .routes import router as user_router
from .database import Base, engine, get_db
# from sqlalchemy.orm import Session
import logging
# import pandas as pd


logging.basicConfig(level=logging.INFO)



# Create tables
Base.metadata.create_all(bind=engine)

base_dir = os.path.dirname(__file__)

csv_path = os.path.join(base_dir,'resources','movies.csv')
print(f"{base_dir} lllll")

# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     # logging.info("Lifespan function is starting")
#     # print(base_dir)
#     df = pd.read_csv(csv_path)
    # print(f"{len(df)} lll")
    # logging.info(f"Loaded DataFrame with {len(df)} rows")
    
    
    
    # with Session(engine) as db:
    #     batch_size = 1000
    #     for i in range(0, len(df), batch_size):
    #         batch = df.iloc[i:i+batch_size]
        
    #         data_to_insert = batch.to_dict(orient="records")
        
    #         db.execute(insert(Movie).values(data_to_insert))
        
    #     db.commit()
    
    # yield

app = FastAPI()

app.include_router(user_router)


