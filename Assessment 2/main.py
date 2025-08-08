from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from moviecollection import MovieCollection
from movie import Movie

class MovieApp(App):
    def build(self):
        self.movie_collection = MovieCollection()
        self.movie_collection.load_movies('movies.json')

        layout = BoxLayout(orientation='horizontal', padding=10, spacing=10)

        # Left side for input and sorting
        left_layout = BoxLayout(orientation='vertical', size_hint=(0.3, 1))

        title_input = TextInput(hint_text="Title", size_hint_y=None, height=40)
        category_spinner = Spinner(values=("Action", "Comedy", "Drama", "Thriller"), size_hint_y=None, height=40)
        year_input = TextInput(hint_text="Year", input_filter='int', size_hint_y=None, height=40)

        add_button = Button(text="Add Movie", size_hint_y=None, height=40)
        add_button.bind(on_press=self.add_movie)

        left_layout.add_widget(title_input)
        left_layout.add_widget(category_spinner)
        left_layout.add_widget(year_input)
        left_layout.add_widget(add_button)

        # Right side for movie buttons and status
        right_layout = BoxLayout(orientation='vertical', size_hint=(0.7, 1))
        self.status_label = Label(text="Movies status", size_hint_y=None, height=40)
        right_layout.add_widget(self.status_label)

        # Movie buttons will be dynamically created here in GridLayout
        self.movie_buttons_layout = GridLayout(cols=1, size_hint_y=None, height=400)
        right_layout.add_widget(self.movie_buttons_layout)

        layout.add_widget(left_layout)
        layout.add_widget(right_layout)

        # Dynamically populate the movie buttons
        self.update_movie_buttons()

        return layout

    def add_movie(self, instance):
        title_input = self.root.children[1].children[4].children[0]
        category_spinner = self.root.children[1].children[4].children[1]
        year_input = self.root.children[1].children[4].children[2]

        title = title_input.text
        category = category_spinner.text
        year = year_input.text

        # Input validation
        if not title or not category or not year:
            self.status_label.text = "All fields must be completed"
            return
        try:
            year = int(year)
        except ValueError:
            self.status_label.text = "Please enter a valid number for year"
            return

        movie = Movie(title, category, year)
        self.movie_collection.add_movie(movie)
        self.update_movie_buttons()

        # Clear input fields
        title_input.text = ""
        category_spinner.text = "Action"
        year_input.text = ""
        self.status_label.text = "Movie added successfully"

    def update_movie_buttons(self):
        # Clear existing buttons
        self.movie_buttons_layout.clear_widgets()

        # Dynamically create movie buttons based on the movie collection
        for movie in self.movie_collection.movies:
            button = Button(text=str(movie), size_hint_y=None, height=40)
            button.bind(on_press=self.toggle_watched_status)
            if movie.watched:
                button.background_color = (0.2, 0.6, 0.2, 1)  # Green for watched
            else:
                button.background_color = (0.6, 0.2, 0.2, 1)  # Red for unwatched
            self.movie_buttons_layout.add_widget(button)

        # Update status label with current movie count
        watched_count = self.movie_collection.get_number_of_watched_movies()
        unwatched_count = self.movie_collection.get_number_of_unwatched_movies()
        self.status_label.text = f"{unwatched_count} movies still to watch, {watched_count} watched"

    def toggle_watched_status(self, instance):
        # Toggle watched status of the clicked movie
        movie_title = instance.text.split('(')[0].strip()
        for movie in self.movie_collection.movies:
            if movie.title == movie_title:
                if movie.watched:
                    movie.mark_unwatched()
                    instance.background_color = (0.6, 0.2, 0.2, 1)
                else:
                    movie.mark_watched()
                    instance.background_color = (0.2, 0.6, 0.2, 1)
                self.status_label.text = f"You have {'watched' if movie.watched else 'unwatched'} {movie_title}"
                break

    def on_stop(self):
        # Save movies data when the app closes
        self.movie_collection.save_movies('movies.json')

if __name__ == '__main__':
    MovieApp().run()