from tkinter import Canvas
from tkinter import Tk
from tkinter import EventType

class Player:
    def __init__(self, _root:Tk, _canvas:Canvas):
        self.root = _root
        self.canvas = _canvas
        self.player = self.canvas.create_rectangle(0, 0, 10, 10, fill='red')
        self.cont_move_left = False
        self.cont_move_right = False
        self.cont_move_down = False
        self.cont_move_up = False
        self.x = 0
        self.y = 0
        self.move_speed = 3

    def move_right(self, event):
        if(event.type == EventType.KeyPress):
            self.cont_move_right = True
            self.start_move_right()

        if(event.type == EventType.KeyRelease):
            self.cont_move_right = False

    def start_move_right(self):
        if (self.cont_move_right):
            self.canvas.move(self.player, self.move_speed, 0)
            self.canvas.update()
            self.x += self.move_speed
            self.root.after(0, self.start_move_right)

    def stop_move_right(self, event):
        self.cont_move_right = False

    def move_left(self, event):
        if (event.type == EventType.KeyPress):
            self.cont_move_left = True
            self.start_move_left()

        if (event.type == EventType.KeyRelease):
            self.cont_move_left = False

    def start_move_left(self):
        if self.cont_move_left:
            self.canvas.move(self.player, -self.move_speed, 0)
            self.canvas.update()
            self.x -= self.move_speed
            print('player x {} y {}'.format(self.x, self.y))
            self.root.after(0, func=self.start_move_left)

    def stop_move_left(self):
        self.cont_move_left = False

    def move_down(self, event):
        if(event.type == EventType.KeyPress):
            self.cont_move_down = True
            self.start_move_down()

        if(event.type == EventType.KeyRelease):
            self.cont_move_down = False

    def start_move_down(self):
        if (self.cont_move_down):
            self.canvas.move(self.player, 0, self.move_speed)
            self.canvas.update()
            self.y += self.move_speed
            self.root.after(0, self.start_move_down)

    def stop_move_down(self, event):
        self.cont_move_down = False

    def move_up(self, event):
        if (event.type == EventType.KeyPress):
            self.cont_move_up = True
            self.start_move_up()

        if (event.type == EventType.KeyRelease):
            self.cont_move_up = False

    def start_move_up(self):
        if (self.cont_move_up):
            self.canvas.move(self.player, 0, -self.move_speed)
            self.canvas.update()
            self.y -= self.move_speed
            self.root.after(0, self.start_move_up)

    def stop_move_up(self, event):
        self.cont_move_up = False