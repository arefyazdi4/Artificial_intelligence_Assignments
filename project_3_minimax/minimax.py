from math import inf
from branch import Branch
from board import BoardTicTak
from square import Square


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
        pass


if __name__ == '__main__':
    game = MiniMax()
    game.start(game.game_tree)
