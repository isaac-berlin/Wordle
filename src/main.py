from tkinter import *
import random
import math
from core import *

WORD = "7"
PADDING_CALCULATION_X = (abs(500 - (76 * len(WORD))))//(len(WORD) * 2)

window = Tk()
window.title("Wordle")
window.configure(background="light grey")
window.geometry("500x500")
window.minsize(500, 500)
window.maxsize(500, 500)


test_label = Label(text="", width=9, height=4)
test_label.grid(column=0, row=0, padx=(PADDING_CALCULATION_X, PADDING_CALCULATION_X), pady=(100, 10))


test_label2 = Label(text="B", width=9, height=4)
test_label2.grid(column=1, row=0, padx=(PADDING_CALCULATION_X, PADDING_CALCULATION_X), pady=(100, 10))


test_label3 = Label(text="C", width=9, height=4)
test_label3.grid(column=2, row=0, padx=(PADDING_CALCULATION_X, PADDING_CALCULATION_X), pady=(100, 10))


test_label4 = Label(text="D", width=9, height=4)
test_label4.grid(column=3, row=0, padx=(PADDING_CALCULATION_X, PADDING_CALCULATION_X), pady=(100, 10))


test_label5 = Label(text="E", width=9, height=4)
test_label5.grid(column=4, row=0, padx=(PADDING_CALCULATION_X, PADDING_CALCULATION_X), pady=(100, 10))


def main():
    window.protocol("WM_DELETE_WINDOW", lambda: window.destroy())

    window.mainloop()


if __name__ == '__main__':
    main()
    foo
    test_arr = make_columns(5, len(WORD), WORD)
    print(test_arr[1][1].color)
    print()
    print(test_arr[0])
    print()
    print(test_row(test_arr, 5, "abcde"))
