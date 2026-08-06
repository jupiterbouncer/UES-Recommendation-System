from load_data import load_ratings
from similarityrecommend import similarity_checker
from visualize import plot_average_ratings

matrix, users, songs = load_ratings()
target = users.index("U001")
dist = similarity_checker(matrix[target], matrix)

plot_average_ratings(matrix, songs)

print(dist)
