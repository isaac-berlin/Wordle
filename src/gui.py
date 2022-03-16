from tkinter import *
from core import *

position = [0, 0]

window = Tk()
window.title("Wordle")
window.configure(background="grey")
window.geometry("500x500")
window.minsize(500, 500)
window.maxsize(500, 500)


def make_gui_row(col_len: int, row_num: int) -> list:
    output_list = []
    for i in range(col_len):
        output_list.append(Label(text="", width=9, height=4, background="white")
                           .grid(column=i, row=row_num, padx=(12, 12), pady=(10, 10)))
    return output_list


def make_gui_board(col_len: int, row_len: int, correct_word: str) -> tuple:
    output_list_gui = []
    output_list_object = make_object_columns(col_len, row_len, correct_word)
    for i in range(col_len):
        output_list_gui.append(make_gui_row(row_len, i))
    return output_list_gui, output_list_object
