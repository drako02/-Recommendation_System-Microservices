import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Function to calculate cosine similarity and fetch recommendations
def get_similar_movies(movie_id: int, genre_matrix: pd.DataFrame, top_n=10):
    similarity = cosine_similarity(genre_matrix)
    similarity_df = pd.DataFrame(similarity, index=genre_matrix.index, columns=genre_matrix.index)

    if movie_id not in similarity_df:
        return []
    
    similar_movies = similarity_df[movie_id].sort_values(ascending=False).iloc[1:top_n + 1]
    return similar_movies.index.tolist()

