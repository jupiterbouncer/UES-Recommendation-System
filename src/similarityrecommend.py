import numpy as np
import pandas as pd

df = pd.read_csv(r"data\UESRecSystemRatings.csv")

# Test run
"""
df = df.set_index("UserID")
Rmatrix = df.to_numpy()
test = Rmatrix[0] - Rmatrix[1]
print(test)
print(np.linalg.norm(test))
row1 = Rmatrix[0]
print(row1)
row2 = Rmatrix[1]
print(row2)
mask = ~np.isnan(row1) & ~np.isnan(row2)
r = row1[mask]
r2 = row2[mask]
print(r)
print(r2)
"""


def euclidean_distance(u, v):
    # Distance between two user rating vectors and ignoring comparisons where at least one song isn't rated
    mask = ~np.isnan(u) & ~np.isnan(v)
    if mask.sum() == 0:
        return np.inf
    else:
        targ_row = u[mask]
        other_row = v[mask]
    return np.linalg.norm(targ_row - other_row)


# Compute pairwise distances between a user and all other user vectors
# using euclidean distance
def similarity_checker(rating_matrix):
    n = rating_matrix.shape[0]  # Getting the number of rows in the matrix
    distances = np.zeros(
        (n, n)
    )  # Setting up a square matrix of zeros initialised with 0s

    # Nested for-loops will index the matrix and calculate the euclidean distance of
    # that row [i] with each song a user can possible have [j] (if any)
    for i in range(n):
        for j in range(n):
            if i != j:  # check to not compute distance between the same vector
                distances[i, j] = euclidean_distance(rating_matrix[i], rating_matrix[j])
    return distances


def k_nearest_users(distance_matrix, user_index, k=3):
    # Return indices of the k closest user to user_index (excluding itself)
    distances = distance_matrix[
        user_index
    ].copy()  # copy the user row to serve as a reference
    distances[user_index] = np.inf  # excludes self by setting index to infinity
    return np.argsort(distances)[
        :k
    ]  # sort by the closest distances and return the highest k indices


def recommend_songs(
    ratings_matrix, distance_matrix, user_index, song_ids, k=3, top_n=3
):
    """
    Recommends songs for a user based on their k nearest neighbors
    Note: Only considers songs the target hasn't rated
    """

    neighbor_indexes = k_nearest_users(distance_matrix, user_index, k=k)
    user_ratings = ratings_matrix[user_index]
