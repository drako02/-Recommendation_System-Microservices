import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
from typing import Tuple
import os

curent_dir = os.path.dirname(__file__)
csv_path = os.path.join(curent_dir, 'movies.csv')
# print(f"{path} ---000")
# print(type(csv_path))

def load_movie_data (path: str = csv_path) -> Tuple[pd.DataFrame, pd.DataFrame]:
    # Load the movie data from the CSV file
    movies = pd.read_csv(path)
    movies['genres'] = movies['genres'].apply(lambda x: x.split('|'))

    mlb = MultiLabelBinarizer()
    genre_matrix = mlb.fit_transform(movies['genres'])
    genre_df = pd.DataFrame(genre_matrix, columns=mlb.classes_, index=movies['movieId'])

    return movies, genre_df

# print(load_movie_data())
