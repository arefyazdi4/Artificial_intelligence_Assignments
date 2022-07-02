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
