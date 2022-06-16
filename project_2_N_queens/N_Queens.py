import os
import time
from stackClass import Stack


class Square:
    QUEEN_STATE = 'Q'
    EMPTY_STATE = 'E'
    UNASSIGNED_STATE = None
    # available pieces Q(queen), K(king),B(bishop),N(knight),R(rook),..

    def __init__(self, coordinate: tuple[int, int], state: str = UNASSIGNED_STATE):
        # state shows if there is in pieces in there None-> unassigned str-> taken
        self.coordinate = coordinate
        self.state = state
        self.threatening_squares: list[Square] = list()
        self.domain = [Square.EMPTY_STATE, Square.QUEEN_STATE]
        # available pieces Q(queen), K(king),B(bishop),N(knight),R(rook),..
        self.predecessor: Square = None  # pointer to the father or root
        self.successors: list[Square] = list()  # list of neighbors square obj

    def __str__(self):
        if self.state == Square.UNASSIGNED_STATE:
            return '.'
        elif self.state == Square.EMPTY_STATE:
            return Square.EMPTY_STATE
        else:
            return self.state
            # available pieces Q(queen), K(king),B(bishop),N(knight),R(rook),..


class ChessBoard:
    def __init__(self, queen_num: int = 4):
        self.queen_num = queen_num  # determine the size of board and max number of queens
        self.board = [[Square(coordinate=(i, j)) for j in range(self.queen_num)] for i in range(self.queen_num)]
        self.set_successors()

    def print_board(self):  # print the current state of cheese board
        os.system('Cls')
        for row in self.board:
            print()  # goes for next row
            for square in row:
                print(square, end='  ')  # goes for next column
        print()

    def __getitem__(self, item: tuple[int, int]):  # return square obj with (i,j) coordinate
        for row in self.board:
            for square in row:
                if square.coordinate == item:
                    return square
        return None

    def set_successors(self):  # for all squares it evaluate their neighbors list
        for row in self.board:
            for square in row:
                (i_cur_square, j_cur_square) = square.coordinate
                for i in range(-1, 2):  # (-1,0,1)
                    for j in range(-1, 2):
                        neighbor = self[(i_cur_square + i, j_cur_square + j)]  # get the square obj with this coordinate
                        if neighbor:  # exist
                            if (i, j) != (0, 0):  # preventing square to have it self as neighbor
                                square.successors.append(neighbor)

    def is_goal(self):  # check if we used all queens or not
        queen_used = 0
        for row in self.board:
            for square in row:
                if square.state == Square.QUEEN_STATE:
                    queen_used += 1
        if queen_used == self.queen_num:
            return True
        else:
            return False

    def assign_state(self, square: Square, state: str):
        if state == Square.EMPTY_STATE:
            current_square = square
            current_square.state = state
            return True

        if state == Square.QUEEN_STATE and square.threatening_squares.__len__() == 0:  # forward checking & backtrack
            current_square = square
            current_square.state = state

            (i_cur_square, j_cur_square) = current_square.coordinate
            for row in self.board:
                for new_square in row:
                    (i_new_square, j_new_square) = new_square.coordinate
                    if i_new_square == i_cur_square or \
                            j_new_square == j_cur_square or \
                            abs(i_cur_square - i_new_square) == abs(j_cur_square - j_new_square):
                        new_square.domain = [Square.EMPTY_STATE]
                        new_square.threatening_squares.append(current_square)
            return True
        return False  # if state is queen bt square is threatening

    def un_assign_state(self, square: Square):
        current_square = square
        state = current_square.state
        current_square.state = Square.UNASSIGNED_STATE

        if state == Square.QUEEN_STATE:  # forward checking
            (i_cur_square, j_cur_square) = current_square.coordinate
            for row in self.board:
                for new_square in row:
                    (i_new_square, j_new_square) = new_square.coordinate
                    if i_new_square == i_cur_square or \
                            j_new_square == j_cur_square or \
                            abs(i_cur_square - i_new_square) == abs(j_cur_square - j_new_square):
                        new_square.domain = [Square.EMPTY_STATE, Square.QUEEN_STATE]
                        new_square.threatening_squares.remove(current_square)

    def dfs_cps(self, start_square: tuple[int, int] = (0, 0)):
        # solving n queen problem with back tracking and forward cheeking
        pending_squares_stack = Stack()  # [list of tuple(Square obj, acceptable state)]
        current_square: Square = self[start_square]
        pending_squares_stack.push((current_square, Square.EMPTY_STATE))
        pending_squares_stack.push((current_square, Square.QUEEN_STATE))

        while not pending_squares_stack.is_empty():
            if self.is_goal():
                return True
            (square, state) = pending_squares_stack.pop()  # exporting data from stack
            current_square: Square = square  # square obj
            promoted_state: str = state  # square state (pieces at that square) Queen or Empty
            self.print_board()
            time.sleep(0.2)
            print('\n current', current_square.coordinate, current_square.state, state)
            # assign new state to current square and update the domain of hole board squares
            if self.assign_state(square=current_square, state=promoted_state):
                # back tracking if function return false it can't be assigned to queen
                # forward checking to see if neighbor have any valid domain left or not
                neighbor_squares = list(filter(lambda neighbor: neighbor.state == Square.UNASSIGNED_STATE,
                                               current_square.successors))  # list to apply filter on it
                if neighbor_squares:  # exist
                    for neighbor in neighbor_squares:
                        print('neighbor', neighbor.coordinate, neighbor.state, end=' ,, ')
                        neighbor.predecessor = current_square
                        for state in neighbor.domain:
                            pending_squares_stack.push((neighbor, state))
                elif neighbor_squares.__len__() == 0:  # there is no more possible option to do -> dead end
                    self.un_assign_state(current_square)
        return True


if __name__ == '__main__':
    b1 = ChessBoard(queen_num=5)
    b1.dfs_cps((0, 0))
    b1.print_board()
