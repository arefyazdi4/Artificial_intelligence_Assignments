from math import inf


class Square:
    UNSIGNED_STATE = None
    PLAYER_X_STATE = 'X'
    PLAYER_O_STATE = 'O'

    def __init__(self, coordinate: tuple[int, int], state: str = UNSIGNED_STATE):
        self.coordinate = coordinate
        self.state = state

    def __str__(self):
        if self.state == Square.UNSIGNED_STATE:
            return '.'
        else:
            return self.state


class BoardTicTak:
    WIN_STATE = 1
    LOSE_STATE = -1
    DRAW_STATE = 0
    UNSIGNED_STATE = None

    def __init__(self):
        self.state: str = BoardTicTak.UNSIGNED_STATE
        self.board: list[list[Square]] = [[Square(coordinate=(i, j)) for j in range(3)] for i in range(3)]

    def __copy__(self):
        return self.board.copy()

    def __getitem__(self, item: tuple[int, int]):  # return square obj with (i,j) coordinate
        for row in self.board:
            for square in row:
                if square.coordinate == item:
                    return square
        return None

    def __str__(self):
        board: str = str()
        for row in self.board:
            board += '\n'  # goes for next row
            for square in row:
                board += square.__str__() + '  '  # goes for next column
        return board

    def set_state(self):
        for row in self.board:
            for square in row:
                signed_state = square.state
                if signed_state == Square.PLAYER_X_STATE:
                    pass
                elif signed_state == Square.PLAYER_O_STATE:
                    pass


class Branch:
    MODE_MAX = MiniMax.maxi
    MODE_MIN = MiniMax.mini

    def __init__(self, board: BoardTicTak, mode, action:tuple[int,int] ):
        self.board = board
        self.mode = mode
        self.action = action
        self.state = board.state
        if mode == Branch.MODE_MAX:
            self.range = [0, inf]
        else:
            self.range = [-inf, 0]


class MiniMax:
    def __init__(self):
        self.game_tree: Branch = Branch(board=BoardTicTak(), mode=MiniMax.maxi, action=(1, 1))

    def maxi(self):
        pass

    def mini(self):
        pass

    def pruning(self):
        pass

    def start(self, current_branch):



if __name__ == '__main__':
    game = MiniMax()
    game.start(game.game_tree)
