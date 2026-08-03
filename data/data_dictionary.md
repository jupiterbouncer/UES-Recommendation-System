# Data Dictionary

## `UESRecSystemRatings.csv`

| Column                                                     | Type             | Description                                                                                                                                                  |
| ---------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `user_id`                                                  | string           | Unique identifier for each user (e.g.`U001` to `U035`). Row index of the table                                                                               |
| `song_1` to`song_15` <br />(displayed as full song titles) | integer or blank | User's rating of that song on a scale of**0–5**. A **blank/empty cell means the user has not rated that song.** It is treated as missing data (`NaN`), not 0 |

**Rating scale:**

| Value   | Meaning                     |
| ------- | --------------------------- |
| 0       | Disliked strongly           |
| 1       | Disliked                    |
| 2       | Below average               |
| 3       | Average or okay             |
| 4       | Liked                       |
| 5       | Loved                       |
| (blank) | Not rated / not listened to |

**Shape:** 35 users × 15 songs.

**Important:** Missing ratings are not filled in as 0 during analysis as doing so would misrepresent "never listened to" as "hated it" and would distort similarity results. Missing values are handled explicitly too for pairwise-complete comparison.

---

## `songs_metadata.csv`

| Column         | Type    | Description                                                                                                                                      |
| -------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| `song_id`      | string  | Unique identifier for each song (`song_1` to `song_15`). Matches the column headers in `ratings.csv`  used as the join key between the two files |
| `title`        | string  | Song title                                                                                                                                       |
| `artist`       | string  | Performing artist                                                                                                                                |
| `genre`        | string  | Primary genre category (e.g. Hip-Hop, Afrobeats, Pop, Alt, Latin). Used for interpreting whether user clusters align with genre preference       |
| `bpm`          | integer | Beats per minute (tempo) of the track                                                                                                            |
| `duration_sec` | integer | Track length in seconds                                                                                                                          |

**Shape:** 15 songs × 6 fields.

---

## Notes on data generation

This dataset is **synthetic**, generated for the purposes of this project to intentionally include a mix of user patterns to support analysis:

- Several groups of users were generated with strong genre preferences (Hip-Hop, Afrobeats, Pop/Alt), producing tight similarity clusters.
- A small set of users ("twins") were generated with near-identical rating vectors to demonstrate very low Euclidean distance between specific user pairs.
- A few users were given sparse ratings (only 2 - 3 songs rated) to illustrate the cold-start problem in recommendation systems.
- A few users were generated with fully random ratings across all songs, serving as noise with no clear taste pattern.

These patterns are intentional and are referenced when interpreting similarity and recommendation results.
