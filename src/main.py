from gui import *
import random

WORD = "helloo"


def main():
    window.protocol("WM_DELETE_WINDOW", lambda: window.destroy())
    board = make_gui_board(1, 2, WORD)
    print(board[1][0][0].color)
    window.mainloop()


if __name__ == '__main__':
    main()
