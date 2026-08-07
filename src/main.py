from load_data import load_ratings
from similarityrecommend import k_nearest_users, recommend_songs, similarity_checker
from visualize import plot_average_ratings

matrix, users, songs = load_ratings()
distance_matrix = similarity_checker(matrix)

target = users.index("U001")
print(k_nearest_users(distance_matrix, target))

plot_average_ratings(matrix, songs)
recs = recommend_songs(matrix, distance_matrix, target, songs, k=3, top_n=3)

print(f"Recommendation for {users[target]}:")
for song, score in recs:
    print(f"  {song} - predicted rating {score}")
