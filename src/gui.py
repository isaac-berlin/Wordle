from tkinter import *
from tkinter import ttk
from core import *


window = Tk()
window.title("Wordle")
window.configure(background="grey")
window.geometry("500x700")
window.resizable(False, False)


#Label(window, text="Wordle", bg="grey", font=('Comic Sans', 10, 'bold')).pack(anchor=N)


def make_gui_row(col_len: int, row_num: int) -> list:
    output_list = []
    for i in range(col_len):
        output_list.append(Label(text="", fg="black", width=9, height=4, background="white"))
    return output_list


def align_gui(col_len: int, row_num: int, unaligned_list: list):
    for i in range(col_len):
        unaligned_list[i].grid(column=i, row=row_num+1, padx=(12, 12), pady=(10, 10))


def make_gui_board(col_len: int, row_len: int) -> list:
    output_list_gui = []
    for i in range(col_len):
        row = make_gui_row(row_len, i)
        align_gui(row_len, i, row)
        output_list_gui.append(row)
    return output_list_gui


