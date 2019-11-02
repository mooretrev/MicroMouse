from tkinter import Canvas

class Board(Canvas): # inheirating from the Canvas class

    def __init__(self, frame, _player):
        # these will be input from the text file
        WIDTH = 500
        HEIGHT = 500

        # create the canvas
        super().__init__(frame, width = WIDTH, height = HEIGHT)

        self.player = _player

    def read_text_file(self, filename):
        pass


    def create_tape(self, matrix):
        pass




