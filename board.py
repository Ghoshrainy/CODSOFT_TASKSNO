class Board:
    def __init__(self):
        self.cells = [" " for _ in range(9)]

    def display(self):
        print()
        print(f" {self.cells[0]} | {self.cells[1]} | {self.cells[2]} ")
        print("---+---+---")
        print(f" {self.cells[3]} | {self.cells[4]} | {self.cells[5]} ")
        print("---+---+---")
        print(f" {self.cells[6]} | {self.cells[7]} | {self.cells[8]} ")
        print()

    def make_move(self, position, player):
        if self.cells[position] == " ":
            self.cells[position] = player
            return True
        return False

    def is_full(self):
        return " " not in self.cells

    def get_empty_cells(self):
        return [i for i, cell in enumerate(self.cells) if cell == " "]

    def check_winner(self):
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6)
        ]

        for a, b, c in winning_combinations:
            if (
                self.cells[a] != " "
                and self.cells[a] == self.cells[b]
                and self.cells[b] == self.cells[c]
            ):
                return self.cells[a]

        if self.is_full():
            return "Draw"

        return None