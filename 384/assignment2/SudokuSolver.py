import sys
import copy
import time

# this function reads the input file and returns a board with 81 variables
def read_input(file):
    global puzzlenum; # store number of puzzle
    board = [ ['123456789' for x in range(9)] for y in range(9)] # creates all variables with full domain
    x = 0
    y = 0
    f = open(file, 'r')
    for line in f:
        for c in line:
            if c != '\n' and c != ' ':
                if c != '0':
                    board[x][y] = c # assign value to variables already defined in the input
                y += 1
                if (y > 8):
                    y = 0
                    x += 1
    if file=='puzzle1.txt':
        puzzlenum = 1
    elif file=='puzzle2.txt':
        puzzlenum = 2
    elif file=='puzzle3.txt':
        puzzlenum = 3
    elif file=='puzzle4.txt':
        puzzlenum = 4
    elif file=='puzzle5.txt':
        puzzlenum = 5
    f.close()
    return board

# Depth First Search is used here as the brute force approach for solving a puzzle.
# the state and node representations are as follows:
# State = (DOMAINS, (x,y,value))
# Node = (State, ParentNode, depth)
def dfs_search(domains):
    global nodes # keep track of nodes generated
    global performance # file for outputting the performance
    search_start = time.time() # keep track of search time
    expanded = [] # keep track of expanded states
    startingState = [domains, 'no action']
    startingNode = [startingState, 'no parent', 0]
    fringe = [startingNode] # fringe is a stack for the nodes
    nodes = 1 # starting node has been generated
    while (len(fringe) > 0): # while fringe is not empty
        node = fringe.pop() # retrieve top node
        state = node[0]
        board = state[0]
        if not board in expanded:
            expanded.append(copy.deepcopy(board)) # expanding node
            if check_solution(board): # if is a goal state, print search time and nodes and return the completed board
                search_time = ((time.time()-search_start)*1000)
                print("Search clock time: %s" % search_time)
                print("Number of nodes generated: %s" % (nodes))
                performance.write("Search clock time: %s\n" % search_time) # also save these to performance file
                performance.write("Number of nodes generated: %s\n" % (nodes))
                return board
            else: # get successors for this state and insert them into the fringe
                successors = get_successors(board)
                for successor in successors:
                    childNode = [successor, node]
                    childNode.append(node[2]+1)
                    fringe.append(childNode)
                    nodes += 1
    # if no solution found, save performance stats and return failure
    search_time = ((time.time()-search_start)*1000)
    print("Search clock time: %s" % search_time)
    print("Number of nodes generated: %s" % (nodes))
    performance.write("Search clock time: %s\n" % search_time)
    performance.write("Number of nodes generated: %s\n" % (nodes))
    return 'No solution found'

# this function runs through a board and returns true if it is completed according to constraints
def check_solution(domains):
    for x in range(9):
        for y in range(9):
            if len(domains[x][y]) > 1: # if a variable has more than one value in its domain, this puzzle is not solved
                return False
    results = [check_lines(domains), check_squares(domains), check_columns(domains)]
    return all(results) # if all constraint checks return True, the puzzle has been solved

# this function checks all lines for contradictions
def check_lines(domains):
    for i in range(9):
        if not check_line(domains, i):
            return False
    return True

def check_line(domains, i):
    line = list(domains[i][y] for y in range(9))
    if len(line) > len(set(line)):
        return False
    return True

# this function checks all columns for contradictions
def check_columns(domains):
    for i in range(9):
        if not check_column(domains, i):
            return False
    return True

def check_column(domains, i):
    col = list(domains[x][i] for x in range(9))
    if len(col) > len(set(col)):
        return False
    return True

# this function checks all 3x3 squares for contradictions
def check_squares(domains):
    for i in range(3):
        for j in range(3):
            if not check_square(domains, i, j):
                return False
    return True

def check_square(domains, i, j):
    square = []
    for x in range(3):
        for y in range(3):
            square.append(domains[x+i*3][y+j*3])
    if len(square) > len(set(square)):
            return False
    return True

# this function returns possible successors for this board state
# the successors are the possible values for the neighboring variable
def get_successors(board):
    successors = []
    newBoard = copy.deepcopy(board)
    for x in range(9):
        for y in range (9):
            if (len(board[x][y])>1):
                for i in range(1,10):
                    newBoard[x][y] = str(i)
                    successors.append((copy.deepcopy(newBoard), [x,y,str(i)]))
                return successors
    return successors

# this function implements the backtracking search algorithm using CSP
# takes constraint propagation into account but does not use heuristics to choose variables to assign
def backtracking_search(domains):
    global nodes # keep track of nodes generated
    global performance # file for outputting the performance
    search_start = time.time() # keep track of search time
    for i in range(9):
       for j in range(9):
           if len(domains[i][j])==1: # for variables which are assigned by default,
               domains = infer(i, j, domains[i][j], domains) # apply constraint propagation
               if domains == False: # if the inference returns a failure, the board contains an impossible puzzle
                   return 'No solution found'
    nodes = 1 # the board with default constraints applied is the first node
    result = backtrack(domains) # run the recursive backtracking algorithm on the board to find a solution
    search_time = ((time.time()-search_start)*1000)
    print("Search clock time: %s" % search_time) # show search time and nodes generated
    print("Number of nodes generated: %s" % (nodes))
    performance.write("Search clock time: %s\n" % search_time) # also save these to performance file
    performance.write("Number of nodes generated: %s\n" % (nodes))
    if not result==False: # if backtrack returns a solution, return the result
        return result
    return 'No solution found' # if backtrack returns a failure, no solution has been found

# the recursive backtracking algorithm to find a solution for a puzzle board
def backtrack(domains):
    global nodes # keep track of nodes generated
    board = copy.deepcopy(domains) # copy original board for backtracking consistency
    if is_complete(board): # board has been completed. return it as the result
        return board
    x,y = select_next_variable(board) # select next variable to be assigned (no heuristic)
    for value in board[x][y]: # for possible values in the domain, try to assign them
        oldBoard = copy.deepcopy(board) # copy original to make unassignment of values possible
        board[x][y] = value # assign value to variable
        nodes += 1 # this counts as a new node generated
        infered = infer(x, y, value, board) # apply constraints
        if not infered == False: # no contradictions.
            result = backtrack(infered) # recursively run function to assign more variables
            if not result == False:
                return result
        board = oldBoard # contradictions found. backtrack this assignment.
    return False # no viable solution found

# this function checks if all variables have a single value assigned to them
def is_complete(domains):
    for x in range(9):
        for y in range(9):
            if not len(domains[x][y])==1: # has more than one value in domain. unassigned, therefore not complete
                return False
    return True;

# this function selects the next variable to be assigned. no heuristics are used
def select_next_variable(domains):
    for x in range(9):
        for y in range(9):
            if len(domains[x][y])>1: # return next variable tht has not been assigned
                return [x,y]
    return []

# this function applies constraint propagation to a board with a newly assigned variable.
def infer(x, y, value, board):
    infered = copy.deepcopy(board) # copy original for consistency
    infered = infere_square(x,y,value,infered) # apply constraints to square peers
    if infered==False:
        return False
    infered = infere_line(x,y,value,infered) # apply constraints to line peers
    if infered==False:
        return False
    infered = infere_col(x,y,value,infered) # apply constraints to column peers
    if infered==False:
        return False
    return infered # no contradictions found

# this recursive function applies constraint propagation to square peers of an assigned variable
def infere_square(x,y,value,board):
    newBoard = copy.deepcopy(board) # copy for consistency
    sx = 6 # sx and sy for keeping track of which square holds the variable
    sy = 6
    if x<3:
        sx=0
    elif x<6:
        sx=3
    if y<3:
        sy=0
    elif y<6:
        sy=3
    for i in range(3):
        for j in range(3):
            if not (i+sx==x and j+sy==y): # do not apply constraint to the assigned variable
                newDomain = newBoard[i+sx][j+sy].replace(value,'') # remove value from domain
                if len(newDomain)<len(newBoard[i+sx][j+sy]): # domain has changed.
                   newBoard[i+sx][j+sy]=newDomain
                   if (len(newBoard[i+sx][j+sy])==0): # no values left in domain. contradiction. return failure.
                       return False
                   if (len(newBoard[i+sx][j+sy])==1): # only 1 value left in domain. this variable is now assigned
                       newBoard = infer(i + sx, j + sy, newBoard[i + sx][j + sy], newBoard) # apply new constraints
                       if newBoard==False: # contradictions found applying new constraints. return failure.
                           return False
    return newBoard # no contradictions found. return board with constraints applied.

# this recursive function applies constraint propagation to line peers of an assigned variable
def infere_line(x,y,value,board):
    newBoard = copy.deepcopy(board) # copy for consistency
    for j in range(9):
        if not j==y: # do not apply constraint to the assigned variable
            newDomain = newBoard[x][j].replace(value,'') # remove value from domain
            if len(newDomain)<len(newBoard[x][j]): # domain has changed.
                newBoard[x][j] = newDomain
                if (len(newBoard[x][j])==0): # no values left in domain. contradiction. return failure.
                    return False
                if (len(newBoard[x][j])==1): # only 1 value left in domain. this variable is now assigned
                    newBoard = infer(x, j, newBoard[x][j], newBoard) # apply new constraints
                    if newBoard==False: # contradictions found applying new constraints. return failure.
                        return False
    return newBoard # no contradictions found. return board with constraints applied.

# this recursive function applies constraint propagation to column peers of an assigned variable
def infere_col(x,y,value,board):
    newBoard = copy.deepcopy(board) # copy for consistency
    for i in range(9):
        if not i==x: # do not apply constraint to the assigned variable
            newDomain = newBoard[i][y].replace(value,'') # remove value from domain
            if len(newDomain)<len(newBoard[i][y]): # domain has changed.
                newBoard[i][y] = newDomain
                if (len(newBoard[i][y])==0): # no values left in domain. contradiction. return failure.
                    return False
                if (len(newBoard[i][y])==1): # only 1 value left in domain. this variable is now assigned
                    newBoard = infer(i, y, newBoard[i][y], newBoard) # apply new constraints
                    if newBoard==False: # contradictions found applying new constraints. return failure.
                        return False
    return newBoard # no contradictions found. return board with constraints applied.

# this function implements the backtracking search algorithm using CSP with forward checking
# takes constraint propagation into account and uses MRV heuristics when choosing the next variables to be assigned.
# works the same way as backtracking search but uses fc_mrv as its backtracking function
def fc_mrv_search(domains):
    global nodes
    global performance
    search_start = time.time()
    for i in range(9):
       for j in range(9):
           if len(domains[i][j])==1:
               domains = infer(i, j, domains[i][j], domains)
               if domains == False:
                   return 'No solution found'
    nodes = 1
    result =  fc_mrv(domains)
    search_time = ((time.time()-search_start)*1000)
    print("Search clock time: %s" % search_time)
    print("Number of nodes generated: %s" % (nodes))
    performance.write("Search clock time: %s\n" % search_time)
    performance.write("Number of nodes generated: %s\n" % (nodes))
    if not result==False:
        return result
    return 'No solution found'

# the recursive backtracking algorithm to find a solution for a puzzle board.
# works in the exact same way as backtrack function but uses MRV heuristics function when selecting variable to assign
def fc_mrv(domains):
    global nodes
    board = copy.deepcopy(domains)
    if is_complete(board):
        return board
    x,y = select_next_variable_mrv(board) # selects next variable to be assigned using MRV heuristic
    for value in board[x][y]:
        oldBoard = copy.deepcopy(board)
        board[x][y] = value
        nodes += 1
        infered = infer(x, y, value, board)
        if infered != False:
            result = fc_mrv(infered)
            if result != False:
                return result
        board = oldBoard
    return False

# this function returns the next variable to be assigned.
# selects the variable with the smallest domain.
def select_next_variable_mrv(domains):
    smallest = '1234567890'
    smallvar = []
    for x in range(9):
        for y in range (9):
            if len(domains[x][y])>1 and len(domains[x][y])<len(smallest):
                smallest = domains[x][y]
                smallvar = [x,y]
    return smallvar

# this function prints the solved puzzle board and saves output to solution file
def show_board(board):
    global solution # file for outputting solution
    if board=='No solution found': # algorithm returned a failure
        print board # print failure
        solution.write(board) # save failure to file
    else:
        for i in range(9):
            for j in range(9):
                print board[i][j],' ', # print all values
                solution.write(board[i][j]) # also save them to solution file
                solution.write(' ')
            print ''
            solution.write('\n')

# this function parses the command line arguments to choose a search function
def opt():
    return {
        'BF' : 0,
        'BT' : 1,
        'FC-MRV' : 2,
    }.get(sys.argv[2], 1)

puzzlenum = -1 # checks puzzle name to decide saved file names
board = read_input(sys.argv[1]) # parse the input puzzle file
solfile = 'solution.txt'
perfile = 'performance.txt'
if puzzlenum > 0: # named puzzle. modify save file names
    solfile = 'solution' + str(puzzlenum) + '.txt'
    perfile = 'performance' + str(puzzlenum) + '.txt'
solution = open(solfile, 'w') # file for solution output
performance = open(perfile, 'w') # file for performance output
clock_start = time.time() # keep track of total program time
nodes = 0 # start generated nodes at 0
opt = opt() # parse search function option
if opt==0: # run appropriate search function
    board = dfs_search(board)
elif opt==1:
    board = backtracking_search(board)
else:
    board = fc_mrv_search(board)

show_board(board) # show result

total_clock_time_string = str("Total clock time: %s" % ((time.time()-clock_start)*1000))
print(total_clock_time_string) # show total run time of program

performance.write(total_clock_time_string) # write performance to file

solution.close()
performance.close()


















