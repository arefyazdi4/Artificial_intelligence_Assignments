from branch import Branch
from board import BoardTicTak
from square import Square
import play_ground


class MiniMax:
    def __init__(self):
        pass

    # main function that apply search through all possible actions and return a branch and action that have most benefit
    def maxi(self, branch: Branch) -> tuple[Branch, tuple[int, int]]:
        # list contain a coordinate that is valid for Ai to do a move on it
        possible_actions = branch.board.get_valid_actions()
        # list of branches that is made according to each possible action
        possible_branches = list()
        # list of max profit that we can get from each branch that have been passed to state vale func
        state_values = list()
        # iterate trough actions
        for action in possible_actions:
            # creating branch with current branch board and action that is applied after creation
            new_branch = Branch(board=branch.board, action=action, player_state=Square.PLAYER_X_STATE)
            possible_branches.append(new_branch)
        # iterate through each branch
        for branch in possible_branches:
            branch_state_value = self.get_state_value(branch)
            # for state that is not reached their terminal state we consider them as a worth possible case
            # Loss state for Maxi func and Win state for Mini func
            if branch_state_value == BoardTicTak.UNSIGNED_STATE:
                branch_state_value = BoardTicTak.LOSE_STATE
            state_values.append(branch_state_value)
        # extraction maximum value that we can get from all branches
        max_state_value = BoardTicTak.LOSE_STATE  # set a default value as a worth case
        max_state_value_index = 0  # set default index as a first possible action
        for index, state_value in enumerate(state_values):
            # check if it's max value
            if state_value >= max_state_value:
                max_state_value = state_value
                max_state_value_index = index
        # return beast branch and best action that lead us to best possible state
        return possible_branches[max_state_value_index], possible_actions[max_state_value_index]

    def mini(self, branch: Branch) -> tuple[Branch, tuple[int, int]]:
        possible_actions = branch.board.get_valid_actions()
        possible_branches = list()
        state_values = list()
        for action in possible_actions:
            new_branch = Branch(board=branch.board, action=action, player_state=Square.PLAYER_O_STATE)
            possible_branches.append(new_branch)
        for branch in possible_branches:
            branch.board.set_board_state()
            branch_state_value = self.get_state_value(branch)
            if branch_state_value == BoardTicTak.UNSIGNED_STATE:
                branch_state_value = BoardTicTak.WIN_STATE
            state_values.append(branch_state_value)
        # extraction maximum value that we can get from all branches
        min_state_value = BoardTicTak.WIN_STATE
        min_state_value_index = 0
        for index, state_value in enumerate(state_values):
            if state_value <= min_state_value:
                min_state_value = state_value
                min_state_value_index = index
        return possible_branches[min_state_value_index], possible_actions[min_state_value_index]

    # it get branch and if doesn't have terminal state it applies opposite action aon it
    # if the branch state is considered on getting max value it gone recursively call min value func for it
    def get_state_value(self, branch: Branch) -> int:
        branch.board.set_board_state()
        # check if it's unsigned or not
        if branch.state == BoardTicTak.UNSIGNED_STATE:
            # for branch that made with player O state it gone recall branch to get min on player X state
            if branch.player_state == Square.PLAYER_O_STATE:
                (branch, action_x) = self.maxi(branch)
            # for branch that made with player X state it gone recall branch to get max on player O state
            elif branch.player_state == Square.PLAYER_X_STATE:
                (branch, action_o) = self.mini(branch)
        # return a value that represent of best or possible value possible for branch based of player state
        return branch.state

    def pruning(self):
        pass

    # start's playing game considering that person start firs an as a O player and Ai as a second player and X state
    def start(self):
        # creating new fresh board only for first time game starts
        board = BoardTicTak()
        last_state = board.state  # it's UnSIGNED by default
        print(board)
        # loop keeps going on till one of players Win/Loss or Draw
        while last_state == BoardTicTak.UNSIGNED_STATE:
            # player -> O turn to move
            action_o_str = input('Enter Your Move Coordinate <ij>: ')
            action_o = (int(action_o_str[0]), int(action_o_str[1]))  # ij str to tuple (i,j)
            # apply player move to board and show result
            branch = Branch(board=board, action=action_o, player_state=Square.PLAYER_O_STATE)
            print(branch.board)

            # Ai -> X turn to move
            (branch, action_x) = self.maxi(branch)
            last_state = branch.state
            print(branch.board)


if __name__ == '__main__':
    game = MiniMax()
