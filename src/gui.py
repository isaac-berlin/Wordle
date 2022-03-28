from tkinter import *
from tkinter import ttk
from core import *


window = Tk()
window.title("Wordle")
window.configure(background="grey")
window.geometry("500x700")
window.resizable(False, False)


Label(text="Wordle", fg="black", bg="grey", font=("MSSerif", 50)).place(anchor='n', relx=.5, rely=.1)


def make_gui_row(col_len: int, row_num: int) -> list:
    output_list = []
    for i in range(col_len):
        output_list.append(Label(text="", font="MSSerif", fg="black", background="white"))
    return output_list


def align_gui(col_len: int, row_num: int, unaligned_list: list):
    for i in range(col_len):
        unaligned_list[i].place(x=(90*i)+35, y=((400//5)*row_num)+200, height=70, width=(500//col_len)-30)


def make_gui_board(col_len: int, row_len: int) -> list:
    output_list_gui = []
    for i in range(col_len):
        row = make_gui_row(row_len, i)
        align_gui(row_len, i, row)
        output_list_gui.append(row)
    return output_list_gui
