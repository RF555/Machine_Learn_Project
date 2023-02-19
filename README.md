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
* `genre` - 1/0 for each genre from the playlists above.
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

#### 1. Given this Data Base, could we successfully (with good probability) classify a song to one of these genres?

#### 2. Does one of the algorithms we used worked better than the others? If so why?

#### 3. Which of the parameters of the songs have the most effect of the classification?

#### 4. Can we make a comparison of algorithms by there accuracy?

#### 5. Can we add more parameters so that we'll get better results?

#### 6. 

## Authors

___
Roey Feingold https://github.com/RF555

Yohai Hadad https://github.com/yoyo150696

### Credits

* We used and imported the Python library `Spotipy`. Documentation found here: https://spotipy.readthedocs.io/en/2.22.0/
* We were inpired by the code found here: https://opendatascience.com/a-machine-learning-deep-dive-into-my-spotify-data/