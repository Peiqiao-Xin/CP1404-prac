class Movie:
    def __init__(self, title, category, year, watched=False):
        """
        Initialize the Movie object.
        :param title: The title of the movie
        :param category: The category of the movie (Action, Comedy, etc.)
        :param year: The year the movie was released
        :param watched: Boolean to mark the movie as watched or unwatched (default is False)
        """
        self.title = title
        self.category = category
        self.year = year
        self.watched = watched

    def __str__(self):
        """Return the string representation of the movie."""
        return f"{self.title} ({self.year} {self.category})"

    def mark_watched(self):
        """Mark the movie as watched."""
        self.watched = True

    def mark_unwatched(self):
        """Mark the movie as unwatched."""
        self.watched = False