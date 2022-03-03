import tkinter as tk
import random


class Cube:
    def __init__(self, row: int, position: int, correct_word: str):
        self.row = row
        self.position = position
        self.correct_word = correct_word
        self.correct_letter = correct_word[position]

    def check(self, guess: str) -> str:
        if guess[self.position] not in self.correct_word:
            return "grey"
        elif guess[self.position] in self.correct_word and guess[self.position] != self.correct_letter:
            return "yellow"
        elif guess[self.position] == self.correct_letter:
            return "green"


def make_row(row_num: int, length: int, correct_word: str) -> list:
    row = []
    for i in range(length):
        row_cube = Cube(row_num, i, correct_word)
        row.append(row_cube)
    return row


def make_columns(num_of_col: int, length_of_rows: int, correct_word: str) -> list:
    arr = []
    for i in range(num_of_col):
        arr.append(make_row(i, length_of_rows, correct_word))
    return arr

def test_row(object_to_test: list, row_num: int, word_to_test: str) -> list:
    row_output = []


test_arr = make_columns(5, 5, "hello")
print(test_arr[1][1].check("abcde"))
print()
print(test_arr[0])
print()
print(test_arr)