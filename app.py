import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st


df = pd.read_csv('movies.csv')
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

for feature in selected_features:
    df[feature] = df[feature].fillna('')

combined_feat = df['genres']+' '+df['keywords']+' '+df['tagline']+' '+df['cast']+' '+df['director']
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()

feature_vectors = vectorizer.fit_transform(combined_feat)

similarity = cosine_similarity(feature_vectors)

st.title("Movie Recommendation System")
nav = st.sidebar.radio("Navigation", ["Home"])


if nav == 'Home':
    try:
        movie_name = st.text_input("Enter name of the movie that you like :")
        list_of_titles = df['title'].to_list()
        import difflib
        find_match = difflib.get_close_matches(movie_name, list_of_titles)
        close_match = find_match[0]
        movie_index = df[df.title == close_match]['index'].values[0]
        similarity_score = list(enumerate(similarity[movie_index]))
        sorted_similar = sorted(similarity_score, key = lambda x:x[1], reverse = True)
        st.write('Movies you should watch :')
        i = 1
        for j in range (1, len(sorted_similar)) :
            index = sorted_similar[j][0]
            title_from_index = df[df.index == index]['title'].values[0]
            if (i<6):
                st.write(i,'.',title_from_index)
                i = i+1

    except: 
        st.error("Enter a movie title")