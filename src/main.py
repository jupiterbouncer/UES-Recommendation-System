from load_data import load_ratings
from similarityrecommend import similarity_checker

matrix, users, songs = load_ratings()
target = users.index("U001")
dist = similarity_checker(matrix[target], matrix)

print(dist)
