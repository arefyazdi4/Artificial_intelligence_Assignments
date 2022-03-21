from search import SearchProblem
from game import Directions
from util import Stack, Queue


def get_direction(action:str):
    if action == 'South':
        return Directions.SOUTH
    elif action == 'North':
        return Directions.NORTH
    elif action == 'West':
        return Directions.WEST
    elif action == 'East':
        return Directions.EAST


def get_last_state(state: tuple, action):
    if action == Directions.SOUTH:
        state[1] += 1
        return state
    elif action == Directions.NORTH:
        state[1] -= 1
        return state
    elif action == Directions.WEST:
        state[0] += 1
        return state
    elif action == Directions.EAST:
        state[0] -= 1
        return state


def get_new_state(state: tuple, action):
    if action == Directions.SOUTH:
        state[1] -= 1
        return state
    elif action == Directions.NORTH:
        state[1] += 1
        return state
    elif action == Directions.WEST:
        state[0] -= 1
        return state
    elif action == Directions.EAST:
        state[0] += 1
        return state


def depthFirstSearch(problem: SearchProblem):
    problem = SearchProblem()
    current_state = problem.getStartState()
    passed_actions = list()
    pending_actions = Stack()
    while not problem.isGoalState(current_state):
        next_steps = problem.getSuccessors(current_state)
        if next_steps:
            for successor, action, step_cost in next_steps:
                pending_actions.push(get_direction(action=action))
        else:  # in case that we don't have any way
            last_action = passed_actions.pop()
            current_state = get_last_state(state=current_state, action=last_action)
        new_action = pending_actions.pop()
        passed_actions.append(new_action)
        current_state = get_new_state(state=current_state, action=new_action)

    return passed_actions


if __name__ == '__main__':
    import numpy as np
    raw_matrix_1 = np.zeros((3, 2), dtype=int)
    print(raw_matrix_1)
    print(raw_matrix_1.dtype)

    raw_matrix_2 = np.array([2,5])

    print(raw_matrix_2 - raw_matrix_1)
    np.zeros()