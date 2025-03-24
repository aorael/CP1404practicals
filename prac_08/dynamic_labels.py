from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty

class DynamicWidgetsApp(App):
    status_text = StringProperty()
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.name_to_phone = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.display_dictionary()
        return self.root

    def display_dictionary(self):
        """Display dictionary items as labels"""
        for name,phone in self.name_to_phone.items():
            label_text = f"{name}: {phone}"
            temp_label = Label(text=label_text)
            self.root.ids.main.add_widget(temp_label)


DynamicWidgetsApp().run()
