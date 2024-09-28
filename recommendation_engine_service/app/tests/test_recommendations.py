from app.core.recommendation import get_similar_movies
import pandas as pd

# Mock Data for Testing
def mock_genre_matrix():
    data = {
        'Action': [1, 0, 0],
        'Comedy': [0, 1, 0],
        'Drama': [0, 0, 1],
    }
    df = pd.DataFrame(data, index=[1, 2, 3])  # Mock movie IDs
    return df

def test_get_similar_movies():
    # Mock genre matrix
    genre_matrix = mock_genre_matrix()
    movie_id = 1
    top_n = 2

    # Call the recommendation function
    result = get_similar_movies(movie_id, genre_matrix, top_n)

    # Assert that the number of recommendations is equal to top_n
    assert len(result) == top_n

    # Optionally check specific movie IDs in the result
    assert result == [2, 3]  # Example of what you might expect

