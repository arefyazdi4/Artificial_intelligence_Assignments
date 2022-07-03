from square import Square


class BoardTicTak:
    WIN_STATE = 1
    LOSE_STATE = -1
    DRAW_STATE = 0
    UNSIGNED_STATE = None

    def __init__(self):
        self.state: int = BoardTicTak.UNSIGNED_STATE
        self.board: list[list[Square]] = [[Square(coordinate=(i, j)) for j in range(3)] for i in range(3)]

    def __copy__(self):
        new_board = BoardTicTak()
        new_board.board = self.board
        new_board.state = self.board
        return new_board

    def get_square(self, item: tuple[int, int]):  # return square obj with (i,j) coordinate
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
                if self.get_square((i, 0)) == self.get_square((i, 1)) == self.get_square(
                        (i, 2)) == Square.PLAYER_X_STATE:
                    self.state = BoardTicTak.WIN_STATE
                if self.get_square((i, 0)) == self.get_square((i, 1)) == self.get_square(
                        (i, 2)) == Square.PLAYER_O_STATE:
                    self.state = BoardTicTak.LOSE_STATE
            for j in range(3):  # check for column win
                if self.get_square((0, j)) == self.get_square((1, j)) == self.get_square(
                        (2, j)) == Square.PLAYER_X_STATE:
                    self.state = BoardTicTak.WIN_STATE
                if self.get_square((0, j)) == self.get_square((1, j)) == self.get_square(
                        (2, j)) == Square.PLAYER_O_STATE:
                    self.state = BoardTicTak.LOSE_STATE
            # check for diagonal win
            if self.get_square((0, 0)) == self.get_square((1, 1)) == self.get_square((2, 2)) == Square.PLAYER_X_STATE:
                self.state = BoardTicTak.WIN_STATE
            if self.get_square((0, 0)) == self.get_square((1, 1)) == self.get_square((2, 2)) == Square.PLAYER_O_STATE:
                self.state = BoardTicTak.LOSE_STATE
            if self.get_square((2, 0)) == self.get_square((1, 1)) == self.get_square((0, 2)) == Square.PLAYER_X_STATE:
                self.state = BoardTicTak.WIN_STATE
            if self.get_square((2, 0)) == self.get_square((1, 1)) == self.get_square((0, 2)) == Square.PLAYER_O_STATE:
                self.state = BoardTicTak.LOSE_STATE
            # check if it's draw
            self.state = BoardTicTak.DRAW_STATE
            for row in self.board:
                for square in row:
                    if square == Square.UNSIGNED_STATE:
                        self.state = BoardTicTak.UNSIGNED_STATE
                        break
