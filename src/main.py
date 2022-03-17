from gui import *
import random

WORD = "hello"
position = [0, 0]  # y, x
guess_string = ""


def key_press(event, box_object, gui_object):
    global position
    global guess_string
    if event.char == event.keysym:
        if len(guess_string) < len(WORD):
            guess_string += event.char
            gui_object[position[0]][position[1]].configure(text=event.char)
            position = [position[0], position[1]+1]
    elif event.keysym == "Escape":
        guess_string = ""
        position = [position[0], 0]
    elif event.keysym == "Return":
        test_row(box_object, len(WORD), guess_string)
        guess_string = ""
        position = [position[0]+1, 0]


def main():
    window.protocol("WM_DELETE_WINDOW", lambda: window.destroy())
    board_gui = make_gui_board(6, 5)
    board_object = make_object_columns(6, 5, WORD)
    print(board_gui)
    print(board_object)
    window.bind_all('<Key>', lambda event, arg1=board_object, arg2=board_gui: key_press(event, arg1, arg2))
    window.mainloop()


if __name__ == '__main__':
    main()
