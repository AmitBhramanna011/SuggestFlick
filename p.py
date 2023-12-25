def process(user_movie):    
    import pandas as pd
    import numpy as np
    import difflib
    import matplotlib.pyplot as plt
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    movie=pd.read_csv("movies.csv")
    movie.head()
    movie.shape
    
    # select features
    col=['genres','keywords','director','tagline','cast'] 
    col
    
    # movie.isnull().sum()
    for i in col:
        movie[i].fillna("",inplace=True)
    
    movie.isnull().sum()
    
    combined_data=movie['genres']+movie['keywords']+movie['director']+movie['tagline']+movie['cast']
    combined_data
    
    vectorizer=TfidfVectorizer()
    features_vectors=vectorizer.fit_transform(combined_data)
    
    similarity=cosine_similarity(features_vectors)
    similarity
    
    
    user_movie=user_movie
    user_movie
    all_movies=movie['title'].to_list()
    all_movies
    
    
    close_match_movie=difflib.get_close_matches(user_movie,all_movies)
    if not close_match_movie:
        # Handle the case where no close match is found
        return []
    close_match_movie
    matched_movie=close_match_movie[0]
    matched_movie
    
    matched_movie_index=all_movies.index(matched_movie)
    matched_movie_index
    
    similar_score=list(enumerate(similarity[matched_movie_index]))
    
    len(similar_score)
    
    sorted_similar_score=sorted(similar_score,key=lambda x:x[1])
    sorted_similar_score.reverse()
    sorted_similar_score
    movie['release_date'] = movie['release_date'].str[:4]
    recommended_movies=[]
    ind=1


    for i in range(5):
        m=movie[movie["title"]==all_movies[sorted_similar_score[i][0]]]['release_date'].values[0]
        recommended_movies.append((m,all_movies[sorted_similar_score[i][0]]))
        ind+=1

    return recommended_movies
    
    
print(process("bat"))

