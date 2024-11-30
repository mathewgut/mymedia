from tmdbv3api import TMDb, Movie, TV ,Search, Genre, Discover
# yes this is horrible practice, I know
from api_keys import tmdb_key
tmdb = TMDb()
tmdb.api_key = tmdb_key
movie = Movie()
show = TV()
discover = Discover()

genre = Genre()

def query_movie(movie_title):
    results = movie.search(movie_title)
    return results

def query_show(show_name):
    results = show.search(show_name)
    return results

def query_details_show(show_id):
    details = show.details(show_id)
    return details

def query_details_movie(movie_id):
    details = movie.details(movie_id)
    return details

# TODO: cache every 12 hours
def request_popular_movies():
    results = discover.discover_movies({
    'sort_by': 'popularity.desc',
               'vote_count.gte': 400,
    })
    return results

# TODO: cache every 12 hours
def request_popular_shows():
    results = discover.discover_tv_shows({
    'sort_by': 'popularity.desc',
        'vote_count.gte': 400,
    })
    return results

def request_high_rating_movies():
    results = discover.discover_movies({
        'sort_by': 'vote_average.desc',
                   'vote_count.gte': 400,

    })
    return results

def request_high_rating_shows():
    results = discover.discover_tv_shows({
        'sort_by': 'vote_average.desc',
                   'vote_count.gte': 400,

    })
    return results


"""
note: reconfigure dict to cache. its mostly unchanging, so doing an api call
every time the dict needs to be used is incredibly expensive
"""
def get_movie_genre_dict():
    movie_genres = genre.movie_list()
    genre_dict = {g['id']: g['name'] for g in movie_genres}
    return genre_dict
def get_show_genre_dict():
    show_genres = genre.tv_list()
    genre_dict = {g['id']: g['name'] for g in show_genres}
    return genre_dict


