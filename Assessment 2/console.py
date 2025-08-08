"""
console.py

Command‐line interface for Must-See Movies 2.0
"""
from movie import Movie
from moviecollection import MovieCollection

def display_menu():
    print("\nMust-See Movies 2.0")
    print("L - List movies")
    print("A - Add new movie")
    print("M - Mark a movie as watched")
    print("Q - Quit")

def list_movies(collection: MovieCollection):
    if not collection.movies:
        print("No movies saved")
        return
    for i, m in enumerate(collection.movies, 1):
        print(f"{i}. {m}")

def add_movie(collection: MovieCollection):
    title = input("Title: ").strip()
    year_str = input("Year: ").strip()
    category = input("Category: ").strip().capitalize()
    try:
        year = int(year_str)
    except ValueError:
        print("Invalid year; must be a number")
        return
    if category not in ['Action','Comedy','Documentary','Drama','Fantasy','Thriller']:
        print("Invalid category")
        return
    movie = Movie(title, year, category)
    collection.add_movie(movie)
    print(f"{title} added")

def mark_watched(collection: MovieCollection):
    list_movies(collection)
    choice = input("Enter number to mark as watched: ").strip()
    try:
        idx = int(choice) - 1
        movie = collection.movies[idx]
    except (ValueError, IndexError):
        print("Invalid selection")
        return
    movie.mark_watched()
    print(f"{movie.title} marked as watched")

def main():
    coll = MovieCollection()
    coll.load_movies()
    while True:
        display_menu()
        choice = input(">>> ").strip().upper()
        if choice == 'L':
            list_movies(coll)
        elif choice == 'A':
            add_movie(coll)
        elif choice == 'M':
            mark_watched(coll)
        elif choice == 'Q':
            coll.save_movies()
            print("Goodbye!")
            break
        else:
            print("Invalid option")

if __name__ == '__main__':
    main()