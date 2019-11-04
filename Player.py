from tkinter import Canvas
from tkinter import Event

class Player:
    def __init__(self, _canvas:Canvas):
        self.canvas = _canvas
        self.x:float = 0
        self.y:float = 0
        self.player = self.canvas.create_rectangle(self.x, self.y, 10, 10, fill='red')

    def move_left(self, event):
        print('func called')
        self.x -= 1
        self.canvas.move(self.player, self.x, self.y)
        self.canvas.update()

    def move_right(self, event):
        self.x += 1
        self.canvas.move(self.player, self.x, self.y)
        self.canvas.update()

    def move_down(self, event):
        self.y += 1
        self.canvas.move(self.player, self.x, self.y)
        self.canvas.update()

    def move_up(self, event):
        self.y -= 1
        self.canvas.move(self.player, self.x, self.y)
        self.canvas.update()