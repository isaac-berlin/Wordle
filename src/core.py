class Cube:
    def __init__(self, row: int, position: int, correct_word: str):
        self.row = row
        self.position = position
        self.correct_word = correct_word
        self.correct_letter = correct_word[position]
        self.color = "white"

    def check(self, guess: str):
        if guess[self.position] not in self.correct_word:
            self.color = "grey"
        elif guess[self.position] in self.correct_word and guess[self.position] != self.correct_letter:
            self.color = "yellow"
        elif guess[self.position] == self.correct_letter:
            self.color = "green"


def make_object_row(row_num: int, length: int, correct_word: str) -> list:
    row = []
    for i in range(length):
        row_cube = Cube(row_num, i, correct_word)
        row.append(row_cube)
    return row


def make_object_columns(num_of_col: int, length_of_rows: int, correct_word: str) -> list:
    arr = []
    for i in range(num_of_col):
        arr.append(make_object_row(i, length_of_rows, correct_word))
    return arr


def test_row(object_to_test: list, row_len: int, word_to_test: str):
    for i in range(row_len):
        object_to_test[row_len - 1][i].check(word_to_test)
