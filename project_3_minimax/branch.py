from board import BoardTicTak


# each branch hold a info around their
# uniq game board specific action than have been made an player that made that action
class Branch:
    def __init__(self, board: BoardTicTak, action: tuple[int, int], player_state):
        self.action = action
        self.player_state = player_state
        # creating a new board so that changes doesn't be effected of others
        self.board = board.__copy__()
        # made move on new board
        self.board.get_square(action).state = player_state
        # check a new board state
        self.board.set_board_state()
        # set a branch state a what we get from current board
        self.state = self.board.state
