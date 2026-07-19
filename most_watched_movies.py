# Most Watched Movies
#
# You are given a dictionary where:
#   - The key is a user ID.
#   - The value is a list of movies watched by that user.
#
# A movie should be counted at most once per user, even if that user
# watched it multiple times. Return the movie(s) watched by the
# highest number of *distinct* users (there can be a tie).

from collections import Counter


def most_watched_movies(watch_history):
    movie_count = Counter()

    for movies in watch_history.values():
        movie_count.update(set(movies))  # dedupe repeat watches by the same user

    max_count = max(movie_count.values())

    return [movie for movie, count in movie_count.items() if count == max_count]


watch_history = {
    "user1": ["Inception", "Interstellar", "Inception"],  # rewatched Inception, still counts once
    "user2": ["Avatar", "Inception", "Titanic"],
    "user3": ["Avatar", "Interstellar", "Inception"],
    "user4": ["Inception", "Avatar"],
    "user5": ["Avatar", "Titanic"],
}

print(most_watched_movies(watch_history))
# Output: ['Inception', 'Avatar'] -> both watched by 4 distinct users, so it's a tie


# --- Alternative: plain dict, no imports (what you'd write on a whiteboard) ---
def most_watched_movies_plain(watch_history):
    movie_count = {}

    for movies in watch_history.values():
        for movie in set(movies):
            movie_count[movie] = movie_count.get(movie, 0) + 1

    max_count = max(movie_count.values())

    return [movie for movie, count in movie_count.items() if count == max_count]


print(most_watched_movies_plain(watch_history))
