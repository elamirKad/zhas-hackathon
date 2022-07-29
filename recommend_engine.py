import numpy as np
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class Recommendation:
    def combine_features(self, data):
        features = []
        for i in range(0, data.shape[0]):
            features.append(data['Brand'][i] + ' ' + data['Ingredients'][i]
                            + ' ' + str(data['Combination'][i]) + ' ' + str(data['Dry'][i]) + ' ' + str(
                data['Normal'][i])
                            + ' ' + str(data['Oily'][i]) + ' ' + str(data['Sensitive'][i]))
        return features
    def __init__(self):
        self.df = pd.read_csv('cosmetics_cleaned.csv', encoding='unicode_escape')
        self.columns = ['Brand', 'Ingredients', 'Combination', 'Dry', 'Normal', 'Oily', 'Sensitive']
        self.df['combined_features'] = self.combine_features(self.df)
        self.cm = CountVectorizer().fit_transform(self.df['combined_features'])
        self.cs = cosine_similarity(self.cm)

    def get_recommendation(self, id, max=5):
        cosmetic_id = id
        scores = list(enumerate(self.cs[cosmetic_id]))
        sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
        sorted_scores = sorted_scores[1:max+1]
        return sorted_scores


rec = Recommendation()
for id, value in rec.get_recommendation(1):
    print(id)