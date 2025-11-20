"""
CP1404 Prac_08
Convert miles to kilometres in a Kivy app

"""

CONVERSION_FACTOR = 1.61  # 1.61 kilometers in a mile

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertMiles(App):
    output = StringProperty()

    def build(self):
        """Construct the app."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.output = "Type in the field & press Enter"
        return self.root

    def handle_convert(self):
        """convert user input to kilometers and update label"""
        try:
            miles = float(self.root.ids.user_input.text) * CONVERSION_FACTOR
            self.output = f"{miles}"
        except ValueError:
            self.output = '0.0'

    def handle_increment(self, value):
        """Increment the user input and convert to kilometers"""
        try:
            self.root.ids.user_input.text = str(float(self.root.ids.user_input.text) + value)
            ConvertMiles.handle_convert(self)
        except ValueError:
            self.root.ids.user_input.text = str(value)
            ConvertMiles.handle_convert(self)


ConvertMiles().run()
