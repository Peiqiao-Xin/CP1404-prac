from moviecollection import MovieCollection
from movie import Movie


def main():
    movie_collection = MovieCollection()
    movie_collection.load_movies('movies.json')

    while True:
        print("\nMenu:")
        print("1. Show all movies")
        print("2. Add a new movie")
        print("3. Mark a movie as watched")
        print("4. Mark a movie as unwatched")
        print("5. Show number of watched and unwatched movies")
        print("6. Save and exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            for movie in movie_collection.movies:
                print(movie)
        elif choice == '2':
            title = input("Enter movie title: ")
            category = input("Enter movie category: ")
            year = input("Enter movie year: ")
            try:
                year = int(year)
                movie = Movie(title, category, year)
                movie_collection.add_movie(movie)
            except ValueError:
                print("Please enter a valid year.")
        elif choice == '3':
            title = input("Enter movie title to mark as watched: ")
            for movie in movie_collection.movies:
                if movie.title == title:
                    movie.mark_watched()
                    print(f"{title} marked as watched.")
                    break
            else:
                print(f"No movie found with title {title}.")
        elif choice == '4':
            title = input("Enter movie title to mark as unwatched: ")
            for movie in movie_collection.movies:
                if movie.title == title:
                    movie.mark_unwatched()
                    print(f"{title} marked as unwatched.")
                    break
            else:
                print(f"No movie found with title {title}.")
        elif choice == '5':
            print(
                f"Watched: {movie_collection.get_number_of_watched_movies()} | Unwatched: {movie_collection.get_number_of_unwatched_movies()}")
        elif choice == '6':
            movie_collection.save_movies('movies.json')
            print("Movies saved. Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")