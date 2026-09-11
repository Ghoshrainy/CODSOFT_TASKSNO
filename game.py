from board import Board
from ai import AI


class Game:
    def __init__(self):
        self.board = Board()
        self.ai = AI()

        self.games_played = 0
        self.human_wins = 0
        self.ai_wins = 0
        self.draws = 0

    def human_move(self):
        while True:
            try:
                position = int(input("Enter your move (1-9): ")) - 1

                if position < 0 or position > 8:
                    print("Please enter a number from 1 to 9.")
                    continue

                if self.board.make_move(position, "X"):
                    break

                print("That position is already occupied.")

            except ValueError:
                print("Please enter a valid number.")

    def ai_move(self):
        move = self.ai.get_best_move(self.board)
        self.board.make_move(move, "O")
        print(f"AI chose position {move + 1}.")

    def play(self):
        print("\n===== TIC-TAC-TOE AI =====")
        print("You = X")
        print("AI  = O")

        while True:
            self.board.display()

            self.human_move()

            result = self.board.check_winner()

            if result:
                self.board.display()
                self.show_result(result)
                break

            self.ai_move()

            result = self.board.check_winner()

            if result:
                self.board.display()
                self.show_result(result)
                break

    def show_result(self, result):
        self.games_played += 1

        if result == "X":
            self.human_wins += 1
            print("You win!")

        elif result == "O":
            self.ai_wins += 1
            print("AI wins!")

        else:
            self.draws += 1
            print("It's a draw!")

        print("\n===== SCOREBOARD =====")
        print(f"Games Played : {self.games_played}")
        print(f"Human Wins   : {self.human_wins}")
        print(f"AI Wins      : {self.ai_wins}")
        print(f"Draws        : {self.draws}")