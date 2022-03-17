from tkinter import *
from core import *


window = Tk()
window.title("Wordle")
window.configure(background="grey")
window.geometry("500x700")
window.minsize(500, 700)
window.maxsize(500, 700)


def make_gui_row(col_len: int, row_num: int) -> list:
    output_list = []
    for i in range(col_len):
        output_list.append(Label(text="", width=9, height=4, background="white")
                           .grid(column=i, row=row_num, padx=(12, 12), pady=(10, 10)))
    return output_list


def make_gui_board(col_len: int, row_len: int) -> list:
    output_list_gui = []
    for i in range(col_len):
        output_list_gui.append(make_gui_row(row_len, i))
    return output_list_gui


