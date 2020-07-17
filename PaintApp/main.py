from kivy.app import App
from kivy.uix.widget import Widget

class PaintWindow(Widget):
    pass

class PaintApp(App):
    def build(self):
        return PaintWindow()

PaintApp().run()