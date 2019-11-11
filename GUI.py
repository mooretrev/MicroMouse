from tkinter import *
from Board import Board
from Debounce import Debouncer
from Player import Player

class GUI(Tk):

    def __init__(self):
        super().__init__()
        self.title('Micro Mouse Maze')
        board = Board(self)
        board.pack(expand = True, fill = BOTH)

        # self.debouncer = Debouncer(board.player.key_pressed, board.player.key_released)
        # self.bind('<KeyPress-Right>', self.debouncer.pressed)
        # self.bind('<KeyRelease-Right>', self.debouncer.released)

        debouncer_right = Debouncer(board.player.move_right, board.player.stop_move_right)
        self.bind('<KeyPress-Right>', debouncer_right.pressed)
        self.bind('<KeyRelease-Right>', debouncer_right.released)

        debouncer_left = Debouncer(board.player.move_left, board.player.move_left)
        self.bind('<KeyPress-Left>', debouncer_left.pressed)
        self.bind('<KeyRelease-Left>', debouncer_left.released)

        debouncer_up = Debouncer(board.player.move_up, board.player.move_up)
        self.bind('<KeyPress-Up>', debouncer_up.pressed)
        self.bind('<KeyRelease-Up>', debouncer_up.released)

        debouncer_down = Debouncer(board.player.move_down, board.player.move_down)
        self.bind('<KeyPress-Down>', debouncer_down.pressed)
        self.bind('<KeyRelease-Down>', debouncer_down.released)


        self.mainloop()


    def _pressed_cb(self, event):
        print('Pressed!')

    def _released_cb(self, event):
        print('Released!')