from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    output_text = StringProperty()

    def build(self):
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output_text = '0.0'
        return self.root

    def handle_convert(self):
        self.output_text = str(self.get_valid_miles() * MILES_TO_KM)

    def handle_increment(self, change):
        miles = self.get_valid_miles() + change
        self.root.ids.input_miles.text = str(miles)
        self.output_text = str(miles * MILES_TO_KM)

    def get_valid_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except ValueError:
            return 0.0


MilesConverterApp().run()