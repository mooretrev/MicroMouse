from tkinter import Canvas
from tkinter import Tk
from Tape import Tape
from Player import Player


class Board(Canvas): # inheirating from the Canvas class

    def __init__(self, frame:Tk):
        # these will be input from the text file
        WIDTH = 500
        HEIGHT = 500

        # create the canvas
        super().__init__(frame, width = WIDTH, height = HEIGHT)
        frame.minsize(HEIGHT, WIDTH)

        # create sample tape
        Tape(self, 0,0,25,100)

        # create player
        self.player = Player(frame, self)



    def read_text_file(self, filename):
        pass

    def create_tape(self, matrix):
        pass

    def valid_move(self):
        pass




