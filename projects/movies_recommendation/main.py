import os
from recommender import MovieRecommender

def main():
    recommender = MovieRecommender()
    user_id = input("Enter your user ID: ")
    recommendations = recommender.get_recommendations(user_id)
    print(f"Recommended Movies for User {user_id}:")
    for movie in recommendations:
        print(movie)

if __name__ == "__main__":
    main()
