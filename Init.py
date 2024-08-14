def normalize(value, min_value, max_value):
    return (value - min_value) / (max_value - min_value)


def normalize_songs(songs, user_preferences):
    numerical_cols = ['mixing', 'tempo', 'danceability']
    min_max = {col: (min(song[col] for song in songs), max(song[col] for song in songs)) for col in numerical_cols}

    for song in songs:
        for col in numerical_cols:
            song[col] = normalize(song[col], min_max[col][0], min_max[col][1])

    for col in numerical_cols:
        user_preferences[col] = normalize(user_preferences[col], min_max[col][0], min_max[col][1])


def calculate_numerical_similarity(song, user_preferences):
    numerical_cols = ['mixing', 'tempo', 'danceability']
    similarity = sum((song[col] - user_preferences[col]) ** 2 for col in numerical_cols)
    return 1 - (similarity / len(numerical_cols)) ** 0.5


def calculate_mode_similarity(song_mode, user_mode):
    return 1 if song_mode == user_mode else 0


def calculate_lyrical_similarity(song_lyrics, user_lyrics):
    return len(set(song_lyrics) & set(user_lyrics)) / len(set(song_lyrics) | set(user_lyrics))


def recommend_songs(songs, user_preferences, top_n=3):
    recommendations = []

    for song in songs:
        if song['genre'] != user_preferences['genre']:
            continue

        numerical_similarity = calculate_numerical_similarity(song, user_preferences)
        mode_similarity = calculate_mode_similarity(song['mode'], user_preferences['mode'])
        lyrical_similarity = calculate_lyrical_similarity(song['lyrics'], user_preferences['lyrics'])

        total_similarity = (numerical_similarity + mode_similarity + lyrical_similarity) / 3
        recommendations.append((song, total_similarity))

    #recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations[:top_n]


# Sample song data
songs = [
    {'song_id': 1, 'title': 'Locked out of Heaven', 'mixing': 0.8, 'tempo': 120, 'danceability': 0.9, 'mode': 'Major',
     'genre': 'Pop', 'lyrics': ('Love', 'Resilience', 'Overcoming')},
    {'song_id': 2, 'title': 'Habits', 'mixing': 0.7, 'tempo': 130, 'danceability': 0.8, 'mode': 'Minor', 'genre': 'Pop',
     'lyrics': ('Sad', 'Uncertainty', 'Angry')},
    {'song_id': 3, 'title': 'Sail', 'mixing': 0.6, 'tempo': 110, 'danceability': 0.7, 'mode': 'Major', 'genre': 'Jazz',
     'lyrics': ('Ecstasy', 'Love', 'Happy')},
    {'song_id': 4, 'title': 'Titanium', 'mixing': 0.9, 'tempo': 140, 'danceability': 0.95, 'mode': 'Major',
     'genre': 'Pop', 'lyrics': ('Overcoming', 'Triumphant', 'Resilience')},
    {'song_id': 5, 'title': 'Whistle', 'mixing': 0.7, 'tempo': 125, 'danceability': 0.85, 'mode': 'Minor',
     'genre': 'Jazz', 'lyrics': ('Angry', 'Sad', 'Defeated')}
]

# Sample user preferences
user_preferences = {
    'mixing': 0.75,
    'tempo': 125,
    'danceability': 0.85,
    'mode': 'Major',
    'genre': 'Pop',
    'lyrics': ('Love', 'Resilience', 'Overcoming')
}

normalize_songs(songs, user_preferences)
recommendations = recommend_songs(songs, user_preferences, top_n=3)
for song, similarity in recommendations:
    print(f"Song ID: {song['song_id']}, Title: {song['title']}, Similarity: {similarity:.2f}")
