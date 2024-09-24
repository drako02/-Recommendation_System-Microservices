import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer

def load_movie_data (path: str = '../resources/movies.csv'):
    # Load the movie data from the CSV file
    movies = pd.read_csv(path)
    movies['genres'] = movies['genres'].apply(lambda x: x.split('|'))

    mlb = MultiLabelBinarizer()
    genre_matrix = mlb.fit_transform(movies['genres'])
    genre_df = pd.DataFrame(genre_matrix, columns=mlb.classes_, index=movies['movieId'])

    return movies, genre_df


