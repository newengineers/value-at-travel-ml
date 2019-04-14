import numpy as np
import pandas as pd


def run():
    places_df_path = '../data/data_places.xlsx'
    interests_df_path = '../data/data_interests.xlsx'

    places = pd.read_excel(places_df_path)
    interests = pd.read_excel(interests_df_path)

    places_data = pd.merge(places, interests, on='user')

    #ratings_mean_count = pd.DataFrame(interest_data.groupby('place')['rating'].mean())
    #ratings_mean_count['rating_counts'] = pd.DataFrame(interest_data.groupby('place')['rating'].count())

    user_place_rating = places_data.pivot_table(index='user', columns='place', values='rating')
    print(user_place_rating.head())


run()
