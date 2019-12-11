from tkinter import Canvas
class Tape:

    '''
        Create the tape on the board using a rectangle.
        X is min x
        Y is min y
        Width is max x
        Length is max y
    '''
    def __init__(self, _canvas:Canvas, _x, _y, _width, _length):
        canvas = _canvas
        canvas.create_rectangle(_x, _y, _width, _length, fill='black')
        self.x = _x
        self.y = _y
        self.width = _width
        self.length = _length


    def in_bounds(self, x, y) -> bool:
        return x >= self.x and y >= self.y and x <= self



