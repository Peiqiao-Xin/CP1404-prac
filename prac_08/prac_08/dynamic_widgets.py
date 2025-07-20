from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        self.root = Builder.load_file('dynamic_labels.kv')
        names = ['Alice', 'Bob', 'Charlie', 'Diana']
        for name in names:
            self.root.ids.main.add_widget(Label(text=name))
        return self.root


DynamicLabelsApp().run()