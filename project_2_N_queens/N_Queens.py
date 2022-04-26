import os
import time

from stackClass import Stack


class ChessBoard:
    def __init__(self, queen_num: int = 4):
        self.queen_num = queen_num  # determine the size of board and max number of queens
        self.board = [[Square(coordinate=(i, j)) for j in range(self.queen_num)] for i in range(self.queen_num)]
        self.queen_left = self.queen_num
        self.set_successors()

    def print_board(self):  # print the current state of cheese board
        os.system('Cls')
        for row in self.board:
            print()  # goes for next row
            for square in row:
                print(square, end=' ')  # goes for next column
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
                (x, y) = square.coordinate
                for i in range(-1, 2):  # (-1,0,1)
                    for j in range(-1, 2):
                        neighbor = self[(x + i, y + j)]  # get the square obj with this coordinate
                        if neighbor:  # exist
                            if (i, j) != (0, 0):  # preventing square to have it self as neighbor
                                square.successors.append(neighbor)

    def is_goal(self):  # check if we used all queens or not
        queen_used = 0
        for row in self.board:
            for square in row:
                if square.state == 'Q':
                    queen_used += 1
        if queen_used == self.queen_num:
            return True
        else:
            return False

    def dfs_cps(self, start_square: tuple[int, int] = (0, 0)):
        # solving n queen problem with back tracking and forward cheeking
        passed_squares: list[Square] = list()  # list of (int,int)
        pending_squares = Stack()  # list of State class
        pending_squares.push(self[start_square])

        while not self.is_goal():
            current_square: Square = pending_squares.pop()
            if current_square:
                print('current', current_square.coordinate)
                neighbor_squares = current_square.successors
                if neighbor_squares:
                    for neighbor in neighbor_squares:
                        print('neighbor', neighbor.coordinate)
                        if neighbor not in passed_squares:
                            pending_squares.push(neighbor)
                            print('pending', neighbor.coordinate)

                current_square.state = 'Q'
                passed_squares.append(current_square)
                self.print_board()
                # time.sleep(0.7)


class Square:
    def __init__(self, coordinate: tuple[int, int], state: str = None):
        # state shows if there is in pieces in there None-> vacant str-> taken
        self.coordinate = coordinate
        self.state = state
        self.threatening_squares: list[Square]
        self.domain = ['Q']  # available pieces Q(queen), K(king),B(bishop),N(knight),R(rook),..
        self.predecessor: Square = None   # pointer to the father or root
        self.successors: list[Square] = list()  # list of neighbors square obj

    def __str__(self):
        if self.state:
            return self.state
        else:
            return '.'


if __name__ == '__main__':
    b1 = ChessBoard()
    b1.print_board()
    b1.dfs_cps((0, 0))
