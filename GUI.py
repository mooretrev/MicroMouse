from tkinter import *
from Board import Board
from Player import Player

class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.title('Micro Mouse Maze')
        board = Board(self)
        board.pack(expand = True, fill = BOTH)

        self.bind('a', board.player.move_left)
        self.bind('d', board.player.move_right)
        self.bind('w', board.player.move_up)
        self.bind('s', board.player.move_down)


        self.mainloop()




