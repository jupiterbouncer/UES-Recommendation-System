from load_data import load_ratings
from similarityrecommend import similarity_checker, k_nearest_users
from visualize import plot_average_ratings

matrix, users, songs = load_ratings()
distance_matrix = similarity_checker(matrix)

target = users.index("U001")
print(k_nearest_users(distance_matrix, target))

plot_average_ratings(matrix, songs)
