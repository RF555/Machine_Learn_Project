# Spotify Song Genre Classification

## A Mechine Learn Project

___

## The Data

___
We collected our data from the following generic Spotify playlist:

* [Folk & Acuostic Mix](https://open.spotify.com/playlist/37i9dQZF1EQp62d3Dl7ECY)
* [Pop Mix](https://open.spotify.com/playlist/37i9dQZF1EQncLwOalG3K7)
* [Metal Mix](https://open.spotify.com/playlist/37i9dQZF1EQpgT26jgbgRI)
* [Rock Mix](https://open.spotify.com/playlist/37i9dQZF1EQpj7X7UK8OOF)
* [Hip Hop Mix](https://open.spotify.com/playlist/37i9dQZF1EQnqst5TRi17F)
* [Country Mix](https://open.spotify.com/playlist/37i9dQZF1EQmPV0vrce2QZ)

### Parameters

Each song has the following parameters:

* `id`
* `genre` - ROCK = 1, FOLK_ACUSTIC = 2, POP = 3, METAL = 4, HIP_HOP = 5, COUNTRY = 6.
* `danceability`
* `energy`
* `key`
* `loudness`
* `mode`
* `speechiness`
* `acousticness`
* `instrumentalness`
* `liveness`
* `valence`
* `tempo`
* `duration_ms`
* `time_signature`

All but `id` and `genre` are represented by a numeric value.

## Mechine Learning Algorithms

* Adaboost
* K Nearest Neighbors
* SVM
* Decision Tree

## Our Main Questions

___

### 1. Given this Data Base, could we successfully (with good probability) classify a song to one of these genres?

We found that using Decision Tree we were able to successfuly classify songs by genre with probabilyty 0.65555.

### 2. Does one of the algorithms we used worked better than the others?

The 2 algoritms that wored best were the Decision Tree and SVM (dropping the duration_ms property).

### 3. Which of the parameters of the songs can be dropped to get better classification?

##### Decision Tree

| Number of Properties               | Accuracy | `danceability` | `energy` | `key` | `loudness` | `mode` | `speechiness` | `acousticness` | `instrumentalness` | `liveness` | `valence` | `tempo` | `duration_ms` |
|------------------------------------|----------|----------------|----------|-------|------------|--------|---------------|----------------|--------------------|------------|-----------|---------|---------------|
| 12                                 | 0.61111  |                |          |       |            |        |               |                |                    |            |           |         |               |
| 11<br/>(all marked X are the same) | 0.65555  |                |          |       |            |        |               |                | X                  |            |           |         |               |
| 10                                 | 0.64444  |                |          |       | X          |        |               |                |                    |            |           | X       |               |
| 9                                  | 0.64444  |                |          | X     | X          |        |               |                |                    |            |           | X       |               |
| 8                                  | 0.64444  |                |          | X     | X          |        |               |                |                    | X          |           | X       |               |
| 7                                  | 0.65555  |                |          | X     | X          |        |               |                |                    | X          |           | X       | X             |

##### K Nearest Neighbors

| Number of Properties               | Accuracy | `danceability` | `energy` | `key` | `loudness` | `mode` | `speechiness` | `acousticness` | `instrumentalness` | `liveness` | `valence` | `tempo` | `duration_ms` |
|------------------------------------|----------|----------------|----------|-------|------------|--------|---------------|----------------|--------------------|------------|-----------|---------|---------------|
| 12                                 | 0.3333   |                |          |       |            |        |               |                |                    |            |           |         |               |
| 11<br/>(all marked X are the same) | 0.3333   | X              | X        | X     | X          | X      | X             | X              | X                  | X          | X         | X       | X             |
| 10                                 | 0.3555   |                |          | X     |            |        |               |                |                    |            |           |         | X             |
| 9                                  | 0.5      |                |          | X     |            |        |               |                |                    |            |           | X       | X             |

##### SVM

| Number of Properties | Accuracy | `danceability` | `energy` | `key` | `loudness` | `mode` | `speechiness` | `acousticness` | `instrumentalness` | `liveness` | `valence` | `tempo` | `duration_ms` |
|----------------------|----------|----------------|----------|-------|------------|--------|---------------|----------------|--------------------|------------|-----------|---------|---------------|
| 12                   | 0.21111  |                |          |       |            |        |               |                |                    |            |           |         |               |
| 11                   | 0.6      |                |          |       |            |        |               |                |                    |            |           |         | X             |

##### Adaboost

| Number of Properties | Accuracy | `danceability` | `energy` | `key` | `loudness` | `mode` | `speechiness` | `acousticness` | `instrumentalness` | `liveness` | `valence` | `tempo` | `duration_ms` |
|----------------------|----------|----------------|----------|-------|------------|--------|---------------|----------------|--------------------|------------|-----------|---------|---------------|
| 12                   | 0.43333  |                |          |       |            |        |               |                |                    |            |           |         |               |
| 11                   | 0.46666  |                |          |       |            |        | X             |                |                    |            |           |         |               |
| 10                   | 0.46666  |                | X        |       |            |        | X             |                |                    |            |           |         |               |
| 9                    | 0.46666  |                | X        |       |            |        | X             |                |                    |            |           |         | X             |

In conclusion, we can see that by dropping the property `duration_ms`, the accuracy of all algorithms is improved.

### 4. Can we make a comparison of algorithms by there accuracy?

Our comparison will be of the best result of each algorithm:

| Algo                | Best Accuracy | Dropping                                        |
|---------------------|---------------|-------------------------------------------------|
| Decision Tree       | 0.64444       | `key`, `loudness`, `liveness` and `duration_ms` |
| SVM                 | 0.6           | `duration_ms`                                   |
| K Nearest Neighbors | 0.5           | `key`, `tempo` and `duration_ms`                |
| Adaboost            | 0.46666       | `energy`, `speechiness` and `duration_ms`       |

## Overcoming Overfitting

___

1. Decision Tree - Finding the right depth of the tree.
2. K Nearest Neighbors - Finding the best k for our set of rules.

## Overcoming Other Chalenges

SVM - We found that the property `duration_ms` was problematic with all algorithms, but especially with SVM. After
discovering the problem we were able to get batter results much faster.

## Authors

___
Roey Feingold https://github.com/RF555

Yohai Hadad https://github.com/yoyo150696

### Credits

* We used and imported the Python library `Spotipy`. Documentation found here: https://spotipy.readthedocs.io/en/2.22.0/
* We were inpired by the code found here: https://opendatascience.com/a-machine-learning-deep-dive-into-my-spotify-data/