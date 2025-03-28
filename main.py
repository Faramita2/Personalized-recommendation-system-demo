import os
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns


def load_data():
    ratings = pd.read_csv('data/ratings.csv')
    movies = pd.read_csv('data/movies.csv')
    return pd.merge(ratings, movies, on='movieId')


def preprocess_data(data):
    user_counts = data['userId'].value_counts()
    active_users = user_counts[user_counts >= 30].index

    movie_counts = data['title'].value_counts()
    popular_movies = movie_counts[movie_counts >= 30].index

    filtered_data = data[(data['userId'].isin(active_users)) & (data['title'].isin(popular_movies))]
    filtered_data = filtered_data.groupby(['userId', 'title'], as_index=False).agg({'rating': 'mean', 'timestamp': 'max'})
    filtered_data = filtered_data.sort_values(by='timestamp', ascending=False)
    filtered_data = filtered_data.drop_duplicates(subset=['userId', 'title'], keep='first')

    top_users = user_counts.head(2000).index.union([1])
    top_movies = movie_counts.head(2000).index
    filtered_data = filtered_data[(filtered_data['userId'].isin(top_users)) & (filtered_data['title'].isin(top_movies))]
    return filtered_data


def build_user_movie_matrix(filtered_data):
    user_movie_matrix = filtered_data.pivot(index='userId', columns='title', values='rating')
    return user_movie_matrix.fillna(0).astype(float)


def calculate_user_similarity(user_movie_matrix):
    sparse_matrix = csr_matrix(user_movie_matrix)
    user_similarity = cosine_similarity(sparse_matrix)
    return pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)


def recommend_movies(user_id, user_similarity_df, user_movie_matrix, num_recommendations=5):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:21]
    similar_user_movies = user_movie_matrix.loc[similar_users.index]

    recommended_movies = similar_user_movies.mean(axis=0).sort_values(ascending=False)

    user_rated_movies = user_movie_matrix.loc[user_id].dropna().index
    recommended_movies = recommended_movies.drop(user_rated_movies, errors='ignore')

    if recommended_movies.empty:
        print("No recommendations based on similar users. Falling back to global average ratings.")
        global_avg_ratings = user_movie_matrix.mean(axis=0).sort_values(ascending=False)
        return global_avg_ratings.head(num_recommendations)
    return recommended_movies.head(num_recommendations)


def save_chart_to_file(chart_func, output_dir, file_name, *args):
    plt.figure(figsize=(8, 6))
    chart_func(*args)  
    plt.savefig(os.path.join(output_dir, file_name), bbox_inches='tight')
    plt.close() 


def plot_user_rating_distribution(filtered_data, user_id):
    user_ratings = filtered_data[filtered_data['userId'] == user_id]['rating']
    sns.histplot(user_ratings, bins=10, kde=True, color='blue')
    plt.title(f"Rating Distribution for User {user_id}")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")


def plot_similar_user_ratings(user_similarity_df, user_movie_matrix, user_id):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)[1:21].index
    similar_user_ratings = user_movie_matrix.loc[similar_users].mean(axis=0)
    sns.histplot(similar_user_ratings, bins=10, kde=True, color='green')
    plt.title(f"Average Rating Distribution of Similar Users to User {user_id}")
    plt.xlabel("Rating")
    plt.ylabel("Frequency")


def plot_recommendation_scores(recommendations):
    if recommendations.empty:
        print("No recommendations to plot.")
        return
    sns.barplot(x=recommendations.values, y=recommendations.index, palette="viridis")
    plt.title("Top Recommended Movies and Their Scores")
    plt.xlabel("Average Rating")
    plt.ylabel("Movie Title")


def plot_user_activity(filtered_data):
    user_activity = filtered_data.groupby('userId')['rating'].count().reset_index()
    user_activity.columns = ['userId', 'num_ratings']
    sns.histplot(user_activity['num_ratings'], bins=30, kde=True, color='orange')
    plt.title("User Activity Distribution")
    plt.xlabel("Number of Ratings")
    plt.ylabel("Frequency")


def plot_movie_popularity(filtered_data):
    movie_popularity = filtered_data.groupby('title')['rating'].count().reset_index()
    movie_popularity.columns = ['title', 'num_ratings']
    sns.histplot(movie_popularity['num_ratings'], bins=30, kde=True, color='purple')
    plt.title("Movie Popularity Distribution")
    plt.xlabel("Number of Ratings")
    plt.ylabel("Frequency")


if __name__ == "__main__":
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    data = load_data()

    # data pre-process
    filtered_data = preprocess_data(data)

    # build user-movie matrix
    user_movie_matrix = build_user_movie_matrix(filtered_data)

    # calculate user similarity
    user_similarity_df = calculate_user_similarity(user_movie_matrix)

    user_id = 1
    target_user_data = filtered_data[filtered_data['userId'] == user_id]
    print(f"Number of ratings by user {user_id}: {len(target_user_data)}")

    # generate recommendations for target user
    recommendations = recommend_movies(user_id, user_similarity_df, user_movie_matrix)
    print(f"Top {len(recommendations)} Recommendations for User {user_id}:")
    print(recommendations)

    # save all charts to output folder
    save_chart_to_file(plot_user_rating_distribution, output_dir, "user_rating_distribution.png", filtered_data, user_id)
    save_chart_to_file(plot_similar_user_ratings, output_dir, "similar_user_ratings.png", user_similarity_df, user_movie_matrix, user_id)
    save_chart_to_file(plot_recommendation_scores, output_dir, "recommendation_scores.png", recommendations)
    save_chart_to_file(plot_user_activity, output_dir, "user_activity_distribution.png", filtered_data)
    save_chart_to_file(plot_movie_popularity, output_dir, "movie_popularity_distribution.png", filtered_data)

    print("All charts have been saved to the 'output' folder.")