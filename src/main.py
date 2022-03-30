from gui import *
import random


word_line = random.randint(0, 2314)
with open("../words.txt") as fp:
    for line, word in enumerate(fp):
        if line == word_line:
            WORD = word[:-1]
            print(WORD)
ROW_NUM = 6
position = [0, 0]  # y, x
guess_string = ""
playing_game = True


def key_press(event, box_object, gui_object):
    global position
    global guess_string
    global playing_game
    if event.char == event.keysym and playing_game:
        if len(guess_string) < len(WORD):
            guess_string += event.char.lower()
            gui_object[position[0]][position[1]].configure(text=event.char.upper())
            position = [position[0], position[1]+1]
    elif event.keysym == "BackSpace" and playing_game:
        guess_string = guess_string[:-1]
        gui_object[position[0]][position[1]-1].configure(text="")
        position = [position[0], position[1]-1]
    elif event.keysym == "Return" and playing_game:
        correct_count = 0
        for i in range(len(guess_string)):
            box_object[position[0]][i].check(guess_string)
            gui_object[position[0]][i].config(bg=box_object[position[0]][i].color)
            if box_object[position[0]][i].color == "green":
                correct_count += 1
        guess_string = ""
        if correct_count == len(WORD):
            print("you win")
            playing_game = False
        elif position[0] == ROW_NUM:
            print("you lose")
            playing_game = False
        else:
            position = [position[0]+1, 0]


def main():
    window.protocol("WM_DELETE_WINDOW", lambda: window.destroy())
    board_gui = make_gui_board(ROW_NUM, len(WORD))
    board_object = make_object_columns(ROW_NUM, len(WORD), WORD)
    window.bind_all('<Key>', lambda event, arg1=board_object, arg2=board_gui: key_press(event, arg1, arg2))
    window.mainloop()


if __name__ == '__main__':
    main()
