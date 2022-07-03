from board import BoardTicTak


class Branch:
    def __init__(self, board: BoardTicTak, action: tuple[int, int], player_state):
        self.board = board.__copy__()
        self.board.get_square(action).state = player_state
        self.board.set_board_state()
        self.state = self.board.state
        self.action = action
        self.player_state = player_state
