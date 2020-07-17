from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
# RGBA used to change color and the last one is for opacity of the colors
Window.clearcolor = (0,1,1,1)

class PaintWindow(Widget):
    pass

class PaintApp(App):
    def build(self):
        return PaintWindow()

PaintApp().run()