import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

df=pd.read_csv('indianFood.csv')
class Normal:

    data = df

    def join_columns(X):
        separator = ','
        col_name = 'Overview'
        for i, c in enumerate(X.columns):
            if i == 0:
                X_out = X[c].astype(str).copy()
            else:
                X_out += separator + X[c].astype(str)
        return X_out.to_frame(name=col_name)

    d1 = data.drop("name", axis=1)
    data['Overview'] = join_columns(d1)
    data

    tfidf = TfidfVectorizer(stop_words='english')
    data['Overview'] = data['Overview'].fillna('')
    # Construct the required TF-IDF matrix by applying the fit_transform method on the overview feature
    overview_matrix = tfidf.fit_transform(data['Overview'])
    # Output the shape of tfidf_matrix
    overview_matrix.shape

    similarity_matrix = linear_kernel(overview_matrix, overview_matrix)

    mappingName = pd.Series(data.index, index=data['name'])

    def recommend_food_based_on_plot(self,data_input):
        if(data_input==''):
            return df
        data_index = Normal.mappingName[data_input]
        # get similarity values with other foods
        # similarity_score is the list of index and similarity matrix
        similarity_score = list(enumerate(Normal.similarity_matrix[data_index]))
        # sort in descending order the similarity score of food inputted with all the other foods
        similarity_score = sorted(similarity_score, key=lambda x: x[1], reverse=True)
        # Get the scores of the 15 most similar foods. Ignore the first food.
        similarity_score = similarity_score[0:30]
        # return food names using the mapping series
        data_indices = [i[0] for i in similarity_score]
        return (Normal.data.iloc[data_indices])

# obj=FoodML()
# res=obj.recommend_food_based_on_plot('Tandoori Chicken')
# print(res)

