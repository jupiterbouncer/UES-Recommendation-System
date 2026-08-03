# UES Recommendation System

A linear-algebra-based recommendation system that suggests songs to users based on rating similarity between users (via Euclidean distance).

## Project Structure

```
data/
  ratings.csv          # 35 users x 15 songs rating matrix (0-5, blank = unrated)
  songs_metadata.csv   # song_id, title, artist, genre, bpm, duration_sec
  data_dictionary.md   # column definitions and notes on the dataset

src/
  load_data.py                # loads CSVs into NumPy/pandas structures
  similarityfunctions.py      # Euclidean distance function and generates song recommendations from nearest neighbors
  visualize.py                # bar chart of average rating per song
  main.py                     # runs the full pipeline end-to-end

notebooks/
  exploration_and_results.ipynb            # data sanity checks, early similarity tests
```

## How to Run

```bash
pip install -r requirements.txt
python src/main.py
```

This loads the ratings data, computes user-user similarity, prints sample recommendations for a target user, and displays the average-rating bar chart.

## Approach

1. **Represent ratings as a matrix** - each row is a user, each column a song.
2. **Measure similarity** between users using Euclidean distance between their rating vectors (pairwise-complete, ignoring songs neither user has rated).
3. **Recommend** rated songs to a user based on how their top 3 neighbors rated them.
4. **Visualize** average rating per song as a bar chart.
5. **Interpret** results against song metadata (genre, bpm) to see whether similar users share genre preference.

## Notes

- The dataset is synthetic, generated with intentional patterns to support analysis. See `data/data_dictionary.md` for details.
- Missing ratings are treated as `NaN`, not 0.

## Team

|           Name        | Student ID |
|-----------------------|------------|
|        Kekeli Agblobi |   45862028 |
|  Oluwademilade Subair |   58742028 |
| Ebow Essilfie Quaicoe |   88872028 |
