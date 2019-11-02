from tkinter import Canvas
class Tape:

    def __init__(self, _canvas:Canvas, _x, _y, _width, _length):
        canvas = _canvas
        canvas.create_rectangle(_x, _y, _width, _length)


    def in_bounds(self, x, y) -> bool:
        pass



