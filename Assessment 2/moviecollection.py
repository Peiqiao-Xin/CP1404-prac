import json
from movie import Movie

class MovieCollection:
    def __init__(self):
        """Initialize the MovieCollection with an empty list."""
        self.movies = []

    def add_movie(self, movie):
        """Add a movie to the collection."""
        self.movies.append(movie)

    def get_number_of_unwatched_movies(self):
        """Return the number of unwatched movies in the collection."""
        return len([movie for movie in self.movies if not movie.watched])

    def get_number_of_watched_movies(self):
        """Return the number of watched movies in the collection."""
        return len([movie for movie in self.movies if movie.watched])

    def load_movies(self, filename):
        """Load movies from a JSON file into the collection."""
        try:
            with open(filename, 'r') as file:
                movie_data = json.load(file)
                for data in movie_data:
                    movie = Movie(data['title'], data['category'], data['year'], data['watched'])
                    self.add_movie(movie)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty movie collection.")

    def save_movies(self, filename):
        """Save the movie collection to a JSON file."""
        movie_data = [{
            'title': movie.title,
            'category': movie.category,
            'year': movie.year,
            'watched': movie.watched
        } for movie in self.movies]

        with open(filename, 'w') as file:
            json.dump(movie_data, file, indent=4)

    def sort_movies(self, key):
        """Sort the movies in the collection by the specified key (category or year)."""
        self.movies.sort(key=lambda x: (getattr(x, key), x.title))