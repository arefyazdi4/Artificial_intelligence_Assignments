from minimax import MiniMax
from board import BoardTicTak


class Branch:
    def __init__(self, board: BoardTicTak):
        self.board = board.__copy__()
        self.state = board.state
