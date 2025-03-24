from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """initializes the instance variables"""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

    def handle_greet(self):
        """handles the greeting output"""
        print('test greet')
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """handles clearing the input box"""
        print("test clear")
        self.root.ids.input_name.text = ""




BoxLayoutDemo().run()