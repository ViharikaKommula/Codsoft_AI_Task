import numpy as np
import pandas as pd
movies = pd.read_csv("movies.csv") 
genres = ["Action", "Drama", "Comedy", "Science Fiction", "Horror", "Romance", "Adventure"]
num_users = int(input("Enter the number of users: "))
num_genres = len(genres)
user_genre_matrix = np.zeros((num_users, num_genres), dtype=int)
for i in range(num_users):
    print(f"User {i + 1}:")
    for j, genre in enumerate(genres):
        preference = int(input(f"Enter your preference for {genre} (0 for no, 1 for yes): "))
        user_genre_matrix[i, j] = preference
class RecommendationSystem:
    def __init__(self, user_genre_matrix, movies, genres):
        self.user_genre_matrix = user_genre_matrix
        self.movies = movies
        self.genres = genres
        self.num_users, self.num_genres = user_genre_matrix.shape
    def recommend_movies(self, user_preferences, num_recommendations=3):
        genre_similarity = np.dot(self.user_genre_matrix, user_preferences)
        similar_movies = np.argsort(genre_similarity)[::-1]
        top_movies = similar_movies[:num_recommendations]
        return top_movies
    def get_movie_recommendations(self, user_preferences, num_recommendations=3): 
        recommendations = self.recommend_movies(user_preferences, num_recommendations)
        return recommendations
recommender = RecommendationSystem(user_genre_matrix, movies, genres)
for i in range(num_users):
    user_preferences = user_genre_matrix[i]
    recommendations = recommender.get_movie_recommendations(user_preferences, num_recommendations=3)
    if len(recommendations) > 0:
        print(f"Recommendations for User {i + 1} based on genre preferences:")
        for movie_id in recommendations:
            movie_name = movies.iloc[movie_id]["Movie Title"]
            print(f"Movie: {movie_name}")
    else:
        print(f"No recommendations available for User {i + 1} based on genre preferences.")
