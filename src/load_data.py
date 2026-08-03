import pandas as pd
import numpy as np


# Loading the ratings csv to return a matrix, list of user_ids and song_ids
def load_ratings(filepath="data/UESRecSystemRatings.csv"):
    df = pd.read_csv(filepath, index_col="UserID")
    user_ids = df.index.tolist()
    song_ids = df.columns.tolist()
    matrix = df.to_numpy(dtype=float)  # preserves NaN
    return matrix, user_ids, song_ids


# Loading metadata of songs (genre, bpm, etc)
def load_metadata(filepath="data/songs_metadata.csv"):
    return pd.read_csv(filepath, index_col="song_id")


if __name__ == "__main__":
    matrix, users, songs = load_ratings()
    print(f"Loaded {matrix.shape[0]} users || {matrix.shape[1]} songs")
    print(matrix[0])
