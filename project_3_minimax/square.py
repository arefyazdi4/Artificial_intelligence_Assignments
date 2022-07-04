class Square:
    # all possible states for squares
    UNSIGNED_STATE = None
    PLAYER_X_STATE = 'X'
    PLAYER_O_STATE = 'O'

    # creating square that is cell of board matrix
    def __init__(self, coordinate: tuple[int, int], state: str = UNSIGNED_STATE):
        self.coordinate = coordinate
        self.state = state

    # this function easily represent each square state by the call of print function
    def __str__(self):
        if self.state == Square.UNSIGNED_STATE:
            return '.'
        else:
            return self.state

    # prevention each square to be referenced by making a new obj copy as current and return it
    def __copy__(self):
        new_square = Square(self.coordinate, self.state)
        return new_square
