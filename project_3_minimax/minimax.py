from branch import Branch
from board import BoardTicTak
from square import Square


class MiniMax:
    def __init__(self):
        pass

    def maxi(self, branch: Branch) -> tuple[Branch, tuple[int, int]]:
        pass

    def mini(self):
        pass

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
