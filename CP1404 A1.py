import csv

# Constants
WATCHED = 'w'
UNWATCHED = 'u'


# Function to load movies from a CSV file
def load_movies(filename):
    movies = []
    try:
        with open(filename, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                title, year, category, status = row
                movies.append([title, int(year), category, status])
    except FileNotFoundError:
        print("No movie file found, starting fresh.")
    return movies


# Function to save movies to a CSV file
def save_movies(filename, movies):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        for movie in movies:
            writer.writerow(movie)


# Function to display the movie list
def display_movies(movies):
    unwatched_count = 0
    watched_count = 0
    for index, movie in enumerate(movies, start=1):
        title, year, category, status = movie
        if status == UNWATCHED:
            print(f"{index}. * {title:35} - {year:4} ({category})")
            unwatched_count += 1
        else:
            print(f"{index}.   {title:35} - {year:4} ({category})")
            watched_count += 1
    print(f"{watched_count} movies watched. {unwatched_count} movies still to watch.")


# Function to add a new movie
def add_movie(movies):
    title = input("Title: ").strip()
    while not title:
        print("Input cannot be blank")
        title = input("Title: ").strip()

    year = input("Year: ").strip()
    while not year.isdigit() or int(year) <= 0:
        print("Invalid input; enter a valid number greater than 0")
        year = input("Year: ").strip()
    year = int(year)

    category = input("Category (Action, Comedy, Documentary, Drama, Thriller, Other): ").strip()
    while not category or category not in ["Action", "Comedy", "Documentary", "Drama", "Thriller", "Other"]:
        print("Invalid category; using Other")
        category = "Other"

    movies.append([title, year, category, UNWATCHED])
    print(f"{title} ({category} from {year}) added to movie list")


# Function to mark a movie as watched
def watch_movie(movies):
    if all(movie[3] == WATCHED for movie in movies):
        print("No more movies to watch!")
        return

    try:
        movie_num = int(input("Enter the movie number to mark watched: "))
        if movie_num < 1 or movie_num > len(movies):
            print("Invalid movie number.")
        else:
            if movies[movie_num - 1][3] == WATCHED:
                print("You have already watched this movie.")
            else:
                movies[movie_num - 1][3] = WATCHED
                print(f"{movies[movie_num - 1][0]} ({movies[movie_num - 1][1]}) watched.")
    except ValueError:
        print("Invalid input; enter a valid number")


# Main program
def main():
    filename = 'movies.csv'
    movies = load_movies(filename)

    print("Must-See Movies 1.0 - by [Your Name]")
    print(f"{len(movies)} movies loaded from {filename}")

    while True:
        print("\nMenu:")
        print("D - Display movies")
        print("A - Add new movie")
        print("W - Watch a movie")
        print("Q - Quit")

        choice = input(">>> ").strip().lower()

        if choice == 'd':
            display_movies(movies)
        elif choice == 'a':
            add_movie(movies)
        elif choice == 'w':
            watch_movie(movies)
        elif choice == 'q':
            save_movies(filename, movies)
            print(f"{len(movies)} movies saved to {filename}")
            print("Have a nice day :)")
            break
        else:
            print("Invalid menu choice")


if __name__ == "__main__":
    main()