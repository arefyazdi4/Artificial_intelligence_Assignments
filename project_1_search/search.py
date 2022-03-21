# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem: SearchProblem):
    from game import Directions
    from util import Stack

    class State:  # data model class
        def __init__(self, state_coordinate: tuple[int, int],
                     predecessor=None,
                     action: Directions = None,
                     step_cost=None,
                     successors: list[tuple[int, int]] = None):
            self.state_coordinate = state_coordinate
            self.predecessor: State = predecessor
            self.action: Directions = action
            self.step_cost = step_cost
            self.successors: list[tuple[int, int]] = successors

        def get_path(self):
            action_list: list[Directions] = list()
            current_state = self
            while current_state.action:
                action_list.append(current_state.action)
                current_state = current_state.predecessor
            action_list.reverse()
            return action_list

    current_state = State(problem.getStartState())
    current_state.successors = problem.getSuccessors(current_state.state_coordinate)

    passed_states = list()  # list of (int,int)
    pending_states = Stack()  # list of State class
    pending_states.push(current_state)

    while not problem.isGoalState(current_state.state_coordinate):
        current_state = pending_states.pop()
        if current_state:
            next_steps = current_state.successors
            if next_steps:
                for successor, action, step_cost in next_steps:
                    if successor not in passed_states:
                        new_state = State(state_coordinate=successor,
                                          predecessor=current_state,
                                          action=action,
                                          step_cost=step_cost,
                                          successors=problem.getSuccessors(successor))
                        pending_states.push(new_state)
            passed_states.append(current_state.state_coordinate)
    return current_state.get_path()
    # util.raiseNotDefined()


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    from game import Directions
    from util import Stack,Queue

    class State:  # data model class
        def __init__(self, state_coordinate: tuple[int, int],
                     predecessor=None,
                     action: Directions = None,
                     step_cost=None,
                     successors: list[tuple[int, int]] = None):
            self.state_coordinate = state_coordinate
            self.predecessor: State = predecessor
            self.action: Directions = action
            self.step_cost = step_cost
            self.successors: list[tuple[int, int]] = successors

        def get_path(self):
            action_list: list[Directions] = list()
            current_state = self
            while current_state.action:
                action_list.append(current_state.action)
                current_state = current_state.predecessor
            action_list.reverse()
            return action_list

    current_state = State(problem.getStartState())
    current_state.successors = problem.getSuccessors(current_state.state_coordinate)

    passed_states = list()  # list of (int,int)
    pending_states = Queue()  # list of State class
    pending_states.push(current_state)

    while not problem.isGoalState(current_state.state_coordinate):
        current_state = pending_states.pop()
        if current_state:
            next_steps = current_state.successors
            if next_steps:
                for successor, action, step_cost in next_steps:
                    if successor not in passed_states:
                        new_state = State(state_coordinate=successor,
                                          predecessor=current_state,
                                          action=action,
                                          step_cost=step_cost,
                                          successors=problem.getSuccessors(successor))
                        pending_states.push(new_state)
            passed_states.append(current_state.state_coordinate)
    return current_state.get_path()
    util.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from game import Directions
    from util import Stack, Queue, PriorityQueue

    class State:  # data model class
        def __init__(self, state_coordinate: tuple[int, int],
                     predecessor=None,
                     action: Directions = None,
                     step_cost=None,
                     successors: list[tuple[int, int]] = None):
            self.state_coordinate = state_coordinate
            self.predecessor: State = predecessor
            self.action: Directions = action
            self.step_cost = step_cost
            self.successors: list[tuple[int, int]] = successors

        def get_path(self):
            action_list: list[Directions] = list()
            current_state = self
            while current_state.action:
                action_list.append(current_state.action)
                current_state = current_state.predecessor
            action_list.reverse()
            return action_list

    current_state = State(problem.getStartState())
    current_state.successors = problem.getSuccessors(current_state.state_coordinate)

    passed_states = list()  # list of (int,int)
    pending_states = PriorityQueue()  # list of State class
    pending_states.push(current_state,  0)

    while not problem.isGoalState(current_state.state_coordinate):
        if not pending_states.isEmpty():
            current_state = pending_states.pop()
            passed_states.append(current_state.state_coordinate)
            next_steps = current_state.successors
            if next_steps:
                for successor, action, step_cost in next_steps:
                    if successor not in passed_states:
                        new_state = State(state_coordinate=successor,
                                          predecessor=current_state,
                                          action=action,
                                          step_cost=step_cost,
                                          successors=problem.getSuccessors(successor))
                        pending_states.push(new_state, problem.getCostOfActions(new_state.get_path()))
    return current_state.get_path()

    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
