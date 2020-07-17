from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, Ellipse, Line
# RGBA used to change color and the last one is for opacity of the colors
Window.clearcolor = (0,1,1,1)

class PaintWindow(Widget):
    def on_touch_down(self, touch):
        self.canvas.add(Color(rgb = (1,0,0)))
        d = 30
        self.canvas.add(Ellipse(pos=(touch.x - d/2, touch.y - d/2),size=(d, d)))
        touch.ud['line'] = Line(points=(touch.x, touch.y))
        self.canvas.add(touch.ud['line'])
        print(touch)

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]

class PaintApp(App):
    def build(self):
        return PaintWindow()

PaintApp().run()