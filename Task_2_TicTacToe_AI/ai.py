class AI:
    def __init__(self, ai_player="O", human_player="X"):
        self.ai_player = ai_player
        self.human_player = human_player

    def get_best_move(self, board):
        best_score = float("-inf")
        best_move = None

        for move in board.get_empty_cells():
            board.cells[move] = self.ai_player

            score = self.minimax(board, False)

            board.cells[move] = " "

            if score > best_score:
                best_score = score
                best_move = move

        return best_move

    def minimax(self, board, maximizing):
        result = board.check_winner()

        if result == self.ai_player:
            return 1

        if result == self.human_player:
            return -1

        if result == "Draw":
            return 0

        if maximizing:
            best_score = float("-inf")

            for move in board.get_empty_cells():
                board.cells[move] = self.ai_player
                score = self.minimax(board, False)
                board.cells[move] = " "
                best_score = max(best_score, score)

            return best_score

        best_score = float("inf")

        for move in board.get_empty_cells():
            board.cells[move] = self.human_player
            score = self.minimax(board, True)
            board.cells[move] = " "
            best_score = min(best_score, score)

        return best_score