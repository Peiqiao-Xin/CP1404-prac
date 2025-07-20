from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        # Load the KV layout
        return Builder.load_file('box_layout.kv')

    def handle_greet(self):
        # Greet the user by name
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        # Clear both input and output
        self.root.ids.input_name.text = ''
        self.root.ids.output_label.text = ''


if __name__ == '__main__':
    BoxLayoutDemo().run()
