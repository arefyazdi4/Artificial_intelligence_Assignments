from square import Square


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

    def get_valid_actions(self) -> list[tuple[int, int]]:
        actions = list()
        for row in self.board:
            for square in row:
                if square.state == Square.UNSIGNED_STATE:
                    actions.append(square.coordinate)
        return actions

    def set_board_state(self):  # goes throw board and check if it's win loss draw or unsigned

        if self.state == BoardTicTak.UNSIGNED_STATE:
            for i in range(3):  # check if row is win
                if self[(i, 0)] == self[(i, 1)] == self[(i, 2)] == Square.PLAYER_X_STATE:
                    self.state = BoardTicTak.WIN_STATE
                if self[(i, 0)] == self[(i, 1)] == self[(i, 2)] == Square.PLAYER_O_STATE:
                    self.state = BoardTicTak.LOSE_STATE
            for j in range(3):  # check for column win
                if self[(0, j)] == self[(1, j)] == self[(2, j)] == Square.PLAYER_X_STATE:
                    self.state = BoardTicTak.WIN_STATE
                if self[(0, j)] == self[(1, j)] == self[(2, j)] == Square.PLAYER_O_STATE:
                    self.state = BoardTicTak.LOSE_STATE
            # check for diagonal win
            if self[(0, 0)] == self[(1, 1)] == self[(2, 2)] == Square.PLAYER_X_STATE:
                self.state = BoardTicTak.WIN_STATE
            if self[(0, 0)] == self[(1, 1)] == self[(2, 2)] == Square.PLAYER_O_STATE:
                self.state = BoardTicTak.LOSE_STATE
            if self[(2, 0)] == self[(1, 1)] == self[(0, 2)] == Square.PLAYER_X_STATE:
                self.state = BoardTicTak.WIN_STATE
            if self[(2, 0)] == self[(1, 1)] == self[(0, 2)] == Square.PLAYER_O_STATE:
                self.state = BoardTicTak.LOSE_STATE
            # check if it's draw
            self.state = BoardTicTak.DRAW_STATE
            for row in self.board:
                for square in row:
                    if square == Square.UNSIGNED_STATE:
                        self.state = BoardTicTak.UNSIGNED_STATE
                        break
