from minimax import MiniMax
from board import BoardTicTak
from math import inf


class Branch:
    MODE_MAX = MiniMax.maxi
    MODE_MIN = MiniMax.mini

    def __init__(self, board: BoardTicTak, mode, action: tuple[int, int]):
        self.board = board.__copy__()
        self.mode = mode
        self.action = action
        self.state = board.state
        if mode == Branch.MODE_MAX:
            self.range = [0, inf]
        else:
            self.range = [-inf, 0]
