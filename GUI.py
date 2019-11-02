from tkinter import *
from Board import Board

class GUI(Tk):

    def __init__(self):
        super().__init__()
        board = Board(self)
        board.pack(expand = True, fill = BOTH)
        self.mainloop()




