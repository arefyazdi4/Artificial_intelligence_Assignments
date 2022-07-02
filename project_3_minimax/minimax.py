from branch import Branch
from board import BoardTicTak
from square import Square
import numpy as np


class MiniMax:
    def __init__(self):
        pass

    def maxi(self, branch: Branch) -> tuple[Branch, tuple[int, int]]:
        possible_actions = branch.board.get_valid_actions()
        possible_branches = list()
        state_values = list()
        for action in possible_actions:
            possible_branches.append(Branch(board=branch.board, action=action, player_state=Square.PLAYER_X_STATE))
        for branch in possible_branches:
            state_values.append(self.get_state_value(branch))
        max_value_index = np.argmin(state_values)
        return possible_branches[max_value_index], possible_actions[max_value_index]

    def mini(self, branch: Branch) -> tuple[Branch, tuple[int, int]]:
        pass

    def get_state_value(self, branch: Branch):
        if branch.state == BoardTicTak.UNSIGNED_STATE:
            if branch.player_state == Square.PLAYER_O_STATE:
                (branch, action_x) = self.maxi(branch)
            elif branch.player_state == Square.PLAYER_X_STATE:
                (branch, action_o) = self.mini(branch)
            return branch.state
        else:
            return branch.state

    def pruning(self):
        pass

    def start(self):
        board = BoardTicTak()
        last_state = board.state
        print(board)
        while last_state == BoardTicTak.UNSIGNED_STATE:
            # player -> O turn to move
            action_o_str = input('Enter Your Move <ij>: ')
            action_o = (int(action_o_str[0]), int(action_o_str[1]))  # ij str to tuple (i,j)
            # apply player move to board and show result
            branch = Branch(board=board, action=action_o, player_state=Square.PLAYER_O_STATE)
            print(branch.board)

            # Ai -> X turn to move
            (branch, action_x) = self.maxi(branch)
            board = branch.board
            last_state = branch.state
            print(branch.board)


if __name__ == '__main__':
    game = MiniMax()
    game.start()
