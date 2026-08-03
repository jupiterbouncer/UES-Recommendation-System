import pandas as pd
import numpy as np

df = pd.read_csv(
    r"C:\Users\NEW\OneDrive - Ashesi University\Desktop\2Y SEM 2\Linear Algebra\LA FINAL\UES-Recommendation-System\data\UESRecSystemRatings.csv"
)
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


def similarity_checker(user_row, rating_matrix, user_ids):
    distances = {}
    for i, row in enumerate(rating_matrix):
        mask = ~np.isnan(user_row) & ~np.isnan(rating_matrix[i])
        targ_row = user_row[mask]
        other_row = rating_matrix[i][mask]
        distance = np.linalg.norm(targ_row - other_row)
        if distance > 0:
            distances[user_ids[i]] = distance
    return distances
