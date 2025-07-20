from kivy.app import App
from kivy.lang import Builder


class SquaringApp(App):
    def build(self):
        self.root = Builder.load_file('squaring.kv')
        return self.root

    def handle_calculate(self):
        try:
            value = float(self.root.ids.input_number.text)
            self.root.ids.output_label.text = str(value ** 2)
        except ValueError:
            self.root.ids.output_label.text = 'Invalid input'


SquaringApp().run()