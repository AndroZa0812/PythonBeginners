from data_loader import load_data, preprocess_data

class MovieRecommender:
    def __init__(self):
        self.data = load_data('ratings.csv')
        self.preprocess_data()

    def preprocess_data(self):
        self.data = preprocess_data(self.data)

    def get_recommendations(self, user_id):
        # Implement collaborative filtering algorithm
        pass
