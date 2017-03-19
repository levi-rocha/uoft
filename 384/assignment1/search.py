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
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    "list to store expanded states"
    expanded = []
    
    "create 'state' structure for starting state, including coordinates, no direction and no cost"
    currentPosition = problem.getStartState()
    startingState = []
    startingState.append(currentPosition)
    startingState.append("Stop")
    startingState.append(0)

    "create node structure for starting state, including the state, no parent, and its depth of 0"
    startingNode = [startingState, 'no parent']
    startingNode.append(0)

    "stack to act as fringe, storing nodes to be expanded"
    fringe = util.Stack()

    "push starting node into fringe"
    fringe.push(startingNode)

    "the depthFirstSearch algorithm itself. expands nodes as needed and adds successors to the front of the fringe"
    while not fringe.isEmpty():
        "retrieve the node to be expanded from the fringe"
        currentNode = fringe.pop()
        currentState = currentNode[0]
        currentPosition = currentState[0]
        "if it hasn't already been expanded"
        if not currentPosition in expanded:
            print "expanding: ", currentPosition
            "save this state to the list of expanded states"
            expanded.append(currentPosition)
            print "checking if goal: ", currentPosition
            "if goal state found, calculate and return the path to that state"
            if problem.isGoalState(currentPosition):
                depth = currentNode[2]
                "stack to save nodes in order"
                resultStack = util.Stack()
                while depth > 0:
                    resultStack.push(currentNode)
                    currentNode = currentNode[1]
                    depth -= 1
                "this list will contain the found path to the goal"
                result = []
                "retrieve nodes from the stack and append the necessary actions to the result"
                while not resultStack.isEmpty():
                    node = resultStack.pop()
                    state = node[0]
                    direction = state[1]
                    result.append(direction)
                return result
            else:                
                "retrieve its sucessors"
                children = problem.getSuccessors(currentPosition)
                for successor in children:
                    "create node structure for each sucessor and add them to the fringe"
                    node = [successor, currentNode]
                    successorPosition = successor[0]
                    node.append(currentNode[2]+1)
                    fringe.push(node)
        else:
            print "already expanded: ", currentPosition
    return "no goal found"

    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    "list to store expanded states"
    expanded = []
    
    "create 'state' structure for starting state, including coordinates, no direction and no cost"
    currentPosition = problem.getStartState()
    startingState = []
    startingState.append(currentPosition)
    startingState.append("Stop")
    startingState.append(0)

    "create node structure for starting state, including the state, no parent, and its depth of 0"
    startingNode = [startingState, 'no parent']
    startingNode.append(0)

    "queue to act as fringe, storing nodes to be expanded"
    fringe = util.Queue()

    "push starting node into fringe"
    fringe.push(startingNode)

    "the depthFirstSearch algorithm itself. expands nodes as needed and adds successors to the front of the fringe"
    while not fringe.isEmpty():
        "retrieve the node to be expanded from the fringe"
        currentNode = fringe.pop()
        currentState = currentNode[0]
        currentPosition = currentState[0]
        "if goal state found, calculate and return the path to that state"
        if problem.isGoalState(currentPosition):
            depth = currentNode[2]
            "stack to save nodes in order"
            resultStack = util.Stack()
            resultStack.push(currentNode)
            while depth > 1:
                resultStack.push(currentNode[1])
                currentNode = currentNode[1]
                depth -= 1
            "this list will contain the found path to the goal"
            result = []
            "retrieve nodes from the stack and append the necessary actions to the result"
            while not resultStack.isEmpty():
                node = resultStack.pop()
                state = node[0]
                direction = state[1]
                result.append(direction)
            return result
        else:
            "if it hasn't already been expanded"
            if not currentPosition in expanded:
                "save this state to the list of expanded states"
                expanded.append(currentPosition)
                "retrieve its sucessors"
                children = problem.getSuccessors(currentPosition)
                for successor in children:
                    "create node structure for each sucessor and add them to the fringe"
                    node = [successor, currentNode]
                    node.append(currentNode[2]+1)
                    fringe.push(node)
    return "no goal found"

    util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    "list to store expanded states"
    expanded = []
    
    "create 'state' structure for starting state, including coordinates, no direction and no cost"
    currentPosition = problem.getStartState()
    startingState = []
    startingState.append(currentPosition)
    startingState.append("Stop")
    startingState.append(0)

    "create node structure for starting state, including the state, no parent, its depth of 0 and the total path cost"
    startingNode = [startingState, 'no parent']
    startingNode.append(0)
    startingNode.append(0)

    "priority queue to act as fringe, storing nodes to be expanded"
    fringe = util.PriorityQueue()

    "push starting node into fringe"
    fringe.push(startingNode, 1)

    "the depthFirstSearch algorithm itself. expands nodes as needed and adds successors to the front of the fringe"
    while not fringe.isEmpty():
        "retrieve the node to be expanded from the fringe"
        currentNode = fringe.pop()
        currentState = currentNode[0]
        currentPosition = currentState[0]
        "if goal state found, calculate and return the path to that state"
        if problem.isGoalState(currentPosition):
            depth = currentNode[2]
            "stack to save nodes in order"
            resultStack = util.Stack()
            resultStack.push(currentNode)
            while depth > 1:
                resultStack.push(currentNode[1])
                currentNode = currentNode[1]
                depth -= 1
            "this list will contain the found path to the goal"
            result = []
            "retrieve nodes from the stack and append the necessary actions to the result"
            while not resultStack.isEmpty():
                node = resultStack.pop()
                state = node[0]
                direction = state[1]
                result.append(direction)
            return result
        else:
            "if it hasn't already been expanded"
            if not currentPosition in expanded:
                "save this state to the list of expanded states"
                expanded.append(currentPosition)
                "retrieve its sucessors"
                children = problem.getSuccessors(currentPosition)
                for successor in children:
                    "create node structure for each sucessor and add them to the fringe"
                    node = [successor, currentNode]
                    node.append(currentNode[2]+1)
                    "calculate total path cost and use that as the priority for the node in the fringe"
                    totalCost = currentNode[3] + successor[2]
                    node.append(totalCost)
                    fringe.push(node, totalCost)
    return "no goal found"

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    "list to store expanded states"
    expanded = []
    
    "create 'state' structure for starting state, including coordinates, no direction and no cost"
    currentPosition = problem.getStartState()
    startingState = []
    startingState.append(currentPosition)
    startingState.append("Stop")
    startingState.append(0)

    "create node structure for starting state, including the state, no parent, its depth of 0 and the total path cost"
    startingNode = [startingState, 'no parent']
    startingNode.append(0)
    startingNode.append(0)

    "priority queue to act as fringe, storing nodes to be expanded"
    fringe = util.PriorityQueue()

    "push starting node into fringe"
    fringe.push(startingNode, 1)

    "the depthFirstSearch algorithm itself. expands nodes as needed and adds successors to the front of the fringe"
    while not fringe.isEmpty():
        "retrieve the node to be expanded from the fringe"
        currentNode = fringe.pop()
        currentState = currentNode[0]
        currentPosition = currentState[0]
        "if goal state found, calculate and return the path to that state"
        if problem.isGoalState(currentPosition):
            depth = currentNode[2]
            "stack to save nodes in order"
            resultStack = util.Stack()
            resultStack.push(currentNode)
            while depth > 1:
                resultStack.push(currentNode[1])
                currentNode = currentNode[1]
                depth -= 1
            "this list will contain the found path to the goal"
            result = []
            "retrieve nodes from the stack and append the necessary actions to the result"
            while not resultStack.isEmpty():
                node = resultStack.pop()
                state = node[0]
                direction = state[1]
                result.append(direction)
            return result
        else:
            "if it hasn't already been expanded"
            if not currentPosition in expanded:
                "save this state to the list of expanded states"
                expanded.append(currentPosition)
                "retrieve its sucessors"
                children = problem.getSuccessors(currentPosition)
                for successor in children:
                    "create node structure for each sucessor and add them to the fringe"
                    node = [successor, currentNode]
                    node.append(currentNode[2]+1)
                    "calculate total path cost for priority value"
                    totalCost = currentNode[3] + successor[2]
                    node.append(totalCost)
                    "calculate and include heuristic value in the node's priority in the fringe"
                    heuristicValue = heuristic(successor[0], problem)
                    priority = totalCost + heuristicValue
                    fringe.push(node, priority)
    return "no goal found"


    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
