from tkinter import *
from Board import Board
from Player import Player

class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.title('Micro Mouse Maze')
        player = Player()
        board = Board(self, player)
        board.pack(expand = True, fill = BOTH)
        self.mainloop()




