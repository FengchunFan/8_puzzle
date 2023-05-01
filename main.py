# will build the project based on x, y coordinates
# operators will be based on how 0 moves, thus 4 possible options

# this following puzzle will be used for default goal state
# [[1, 2, 3]]    [[(0,0), (0,1), (0,2)]]
# [[4, 5, 6]] == [[(1,0), (1,1), (1,2)]]
# [[7, 8, 0]]    [[(2,0), (2,1), (2,2)]]

from queue import PriorityQueue #essential for algorithms
import copy
import math #for euclidean distance

# define a Node class to keep track of path used, should have a type puzzle and a node pointer
class Node:
    def __init__(self, puzzle, parent, gcost, hcost):
        self.puzzle = puzzle
        self.parent = parent
        self.gcost = gcost
        self.hcost = hcost

    def __lt__(self, other): # very very important, used for comparison for the priority queue, lower cost = higher priority
        return (self.gcost + self.hcost) < (other.gcost + other.hcost)

# default 3 x 3 puzzle
def print_puzzle(puzzle):
    for i in range(3):
        for j in range(3):
            print(puzzle[i][j], end = " ") #use end = " " to prevent duplicated newlines
        print() #newline

# support function for customized puzzle
def get_row(row_input):
    row = []
    for index in row_input:
        if index.isdigit():
            row.append(index)
    return row

# 4 operators up, down, left, right. But all requires to know 0's position first
# helper function to find where digit lays in the puzzle, type is string btw
def find_zero(puzzle):
    for i in range (3):
        for j in range (3):
            if puzzle[i][j] == '0':
                return i, j

def find_digit(puzzle, digit):
    for i in range (3):
        for j in range (3):
            if puzzle[i][j] == digit:
                return i, j

def zero_up(puzzle):
    i, j = find_zero(puzzle)
    if (i == 0):
        new_puzzle = copy.deepcopy(puzzle) #need to make a hard copy other than referencing back to the input puzzle
        return new_puzzle # no change
    else:
        new_puzzle = copy.deepcopy(puzzle)
        temp = puzzle[i-1][j]
        new_puzzle[i-1][j] = '0'
        new_puzzle[i][j] = temp
        return new_puzzle

def zero_down(puzzle):
    i, j = find_zero(puzzle)
    if (i == 2):
        new_puzzle = copy.deepcopy(puzzle)
        return new_puzzle # no change
    else:
        new_puzzle = copy.deepcopy(puzzle)
        temp = puzzle[i+1][j]
        new_puzzle[i+1][j] = '0'
        new_puzzle[i][j] = temp
        return new_puzzle

def zero_left(puzzle):
    i, j = find_zero(puzzle)
    if (j == 0):
        new_puzzle = copy.deepcopy(puzzle)
        return new_puzzle # no change
    else:
        new_puzzle = copy.deepcopy(puzzle)
        temp = puzzle[i][j-1]
        new_puzzle[i][j-1] = '0'
        new_puzzle[i][j] = temp
        return new_puzzle

def zero_right(puzzle):
    i, j = find_zero(puzzle)
    if (j == 2):
        new_puzzle = copy.deepcopy(puzzle)
        return new_puzzle # no change
    else:
        new_puzzle = copy.deepcopy(puzzle)
        temp = puzzle[i][j+1]
        new_puzzle[i][j+1] = '0'
        new_puzzle[i][j] = temp
        return new_puzzle

#print optimal(hopefully) path
def print_path(node):
    path = []
    temp_node = node #reference the node, we don't want to make changes to the passed-in node
    while temp_node is not None:
        path.append(temp_node.puzzle)
        temp_node = temp_node.parent
    path.reverse() #need to reverse order to display start -> goal
    print("===========")
    for puzzles in path:
        print_puzzle(puzzles)
        print("===========") #puzzle separater
    print("The depth of the goal node was:", len(path)-1) #depth start with first expansion, -1 for initial puzzle

#return h(n) calculated from misplaced tile
def misplace_tile_score(puzzle, goal):
    total = 0
    for digit in range(9):
        i_p, j_p = find_digit(puzzle,str(digit))
        i_g, j_g = find_digit(goal,str(digit))
        temp = abs(i_p - i_g) + abs(j_p - j_g)
        total += temp
    return total

def Euclidean_Distance(puzzle, goal):
    total = 0
    for digit in range(9):
        i_p, j_p = find_digit(puzzle,str(digit))
        i_g, j_g = find_digit(goal,str(digit))
        temp = math.sqrt((i_p - i_g)**2 + (j_p - j_g)**2)
        total += temp
    return total

# Uniform Cost Search: expanding cheapest cost node, depends on g(n) only, h(n) = 0
# reference: https://www.geeksforgeeks.org/priority-queue-using-queue-and-heapdict-module-in-python/
def algo_1(puzzle):
    print("You have chosen the Uniform Cost Search algorithm")
    maximum_nodes = 0 #maximum nodes in q at 1 time
    expanded_nodes = 0 #total nodes expanded
    goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']] #set the goal state
    start_node = Node(puzzle, None, 0, 0) #use the input puzzle to initialize the start node
    q = PriorityQueue()  #create priority queue
    q.put(start_node) #add start_node to the start of the priority queue
    visited_node = [] #add a array to store visited nodes

    while not q.empty(): 
        if(q.qsize() > maximum_nodes):
            maximum_nodes = q.qsize()
        temp_node = q.get() #get the first node off priority queue
        temp_puzzle = temp_node.puzzle #get the puzzle from the node at starting of priority queue
        #uncomment to see the process
        print("The best state to expand with g(n) =", temp_node.gcost)
        print_puzzle(temp_puzzle)
        if(temp_puzzle == goal): #check if is goal
            print("Goal state was reached")
            print_path(temp_node)
            print("The search algorithm expanded a total of", expanded_nodes, "nodes")
            print("The maximum number of nodes in the queue at one time is", maximum_nodes)
            return None #break out of the loop
        possible_moves = [zero_up(temp_puzzle), zero_down(temp_puzzle), zero_left(temp_puzzle), zero_right(temp_puzzle)] #4 operators
        for moves in possible_moves:
            if moves != temp_puzzle: #if there is update in the puzzle, i.e: move is valid
                if moves not in visited_node:
                    expanded_nodes += 1
                    curr_node = Node(moves, temp_node, temp_node.gcost + 1, temp_node.hcost)
                    q.put(curr_node)
                    visited_node.append(moves)

    print("Goal state could not be reached.") #end of the queue has been reached and still not found goal state
    print("The search algorithm expanded a total of", expanded_nodes, "nodes")
    print("The maximum number of nodes in the queue at one time is", maximum_nodes)
    return None

# A* with the Misplaced Tile heuristic, similar as UCS but add h(n)
def algo_2(puzzle):
    print("You have chosen the A* with the Misplaced Tile heuristic algorithm")
    maximum_nodes = 0 #maximum nodes in q at 1 time
    expanded_nodes = 0 #total nodes expanded
    goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']] #set the goal state
    first_h_n = misplace_tile_score(puzzle, goal)
    start_node = Node(puzzle, None, 0, first_h_n) #use the input puzzle to initialize the start node
    q = PriorityQueue()  #create priority queue
    q.put(start_node) #add start_node to the start of the priority queue
    visited_node = [] #add a array to store visited nodes

    while not q.empty(): 
        if(q.qsize() > maximum_nodes):
            maximum_nodes = q.qsize()
        temp_node = q.get() #get the first node off priority queue
        temp_puzzle = temp_node.puzzle #get the puzzle from the node at starting of priority queue
        #uncomment to see the process
        print("The best state to expand with g(n) =", temp_node.gcost, "and h(n) =", temp_node.hcost)
        print_puzzle(temp_puzzle)
        if(temp_puzzle == goal): #check if is goal
            print("Goal state was reached")
            print_path(temp_node)
            print("The search algorithm expanded a total of", expanded_nodes, "nodes")
            print("The maximum number of nodes in the queue at one time is", maximum_nodes)
            return None #break out of the loop
        possible_moves = [zero_up(temp_puzzle), zero_down(temp_puzzle), zero_left(temp_puzzle), zero_right(temp_puzzle)] #4 operators
        for moves in possible_moves:
            if moves != temp_puzzle: #if there is update in the puzzle, i.e: move is valid
                if moves not in visited_node:
                    expanded_nodes += 1
                    h_n = misplace_tile_score(moves, goal)
                    curr_node = Node(moves, temp_node, temp_node.gcost + 1, h_n)
                    q.put(curr_node)
                    visited_node.append(moves)

    print("Goal state could not be reached.") #end of the queue has been reached and still not found goal state
    print("The search algorithm expanded a total of", expanded_nodes, "nodes")
    print("The maximum number of nodes in the queue at one time is", maximum_nodes)
    return None

# A* with the Euclidean distance heuristic, similar to algo 2, just change the h(n) function
def algo_3(puzzle):
    print("You have chosen the A* with the Euclidean distance heuristic algorithm")
    maximum_nodes = 0 #maximum nodes in q at 1 time
    expanded_nodes = 0 #total nodes expanded
    goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']] #set the goal state
    first_h_n = Euclidean_Distance(puzzle, goal)
    start_node = Node(puzzle, None, 0, first_h_n) #use the input puzzle to initialize the start node
    q = PriorityQueue()  #create priority queue
    q.put(start_node) #add start_node to the start of the priority queue
    visited_node = [] #add a array to store visited nodes

    while not q.empty(): 
        if(q.qsize() > maximum_nodes):
            maximum_nodes = q.qsize()
        temp_node = q.get() #get the first node off priority queue
        temp_puzzle = temp_node.puzzle #get the puzzle from the node at starting of priority queue
        #uncomment to see the process
        print("The best state to expand with g(n) =", temp_node.gcost, "and h(n) =", temp_node.hcost)
        print_puzzle(temp_puzzle)
        if(temp_puzzle == goal): #check if is goal
            print("Goal state was reached")
            print_path(temp_node)
            print("The search algorithm expanded a total of", expanded_nodes, "nodes")
            print("The maximum number of nodes in the queue at one time is", maximum_nodes)
            return None #break out of the loop
        possible_moves = [zero_up(temp_puzzle), zero_down(temp_puzzle), zero_left(temp_puzzle), zero_right(temp_puzzle)] #4 operators
        for moves in possible_moves:
            if moves != temp_puzzle: #if there is update in the puzzle, i.e: move is valid
                if moves not in visited_node:
                    expanded_nodes += 1
                    h_n = Euclidean_Distance(moves, goal)
                    curr_node = Node(moves, temp_node, temp_node.gcost + 1, h_n)
                    q.put(curr_node)
                    visited_node.append(moves)

    print("Goal state could not be reached.") #end of the queue has been reached and still not found goal state
    print("The search algorithm expanded a total of", expanded_nodes, "nodes")
    print("The maximum number of nodes in the queue at one time is", maximum_nodes)
    return None

print("Welcome to the 8 puzzle solver")
print("Type “1” to use a default puzzle, or “2” to enter your own puzzle")

puzzle_option = input()
puzzle = []

while(puzzle_option != "1" and puzzle_option != "2"):
    print("Please enter a valid option")
    puzzle_option = input()

if(puzzle_option == "1"):
    #default
    puzzle = [['1', '2', '3'],['4', '8', '0'],['7', '6', '5']]
    print("This will be your starting puzzle:")
    print_puzzle(puzzle)
elif(puzzle_option == "2"):
    #customized puzzle, but does not check legitimacy of the puzzle
    print("Enter your puzzle, use a zero to represent the blank")
    print("Enter the first row, use space or tabs between numbers")
    row_input = input()
    puzzle.append(get_row(row_input))
    print("Enter the second row, use space or tabs between numbers")
    row_input = input()
    puzzle.append(get_row(row_input))
    print("Enter the third row, use space or tabs between numbers")
    row_input = input()
    puzzle.append(get_row(row_input))
    print("This will be your starting puzzle:")
    print_puzzle(puzzle)

# up to this point, the initial puzzle should be formed
print("Enter your choice of algorithm")
print("1. Uniform Cost Search")
print("2. A* with the Misplaced Tile heuristic")
print("3. A* with the Euclidean distance heuristic")

algorithm_option = input()

while(algorithm_option != "1" and algorithm_option != "2" and algorithm_option != "3"):
    print("Please enter a valid option")
    algorithm_option = input()

if(algorithm_option == "1"):
    algo_1(puzzle)
elif(algorithm_option == "2"):
    algo_2(puzzle)
elif(algorithm_option == "3"):
    algo_3(puzzle)

'''
print("Input 1: up, 2: down, 3: left, 4: right, 5: exit")
print_puzzle(puzzle)
temp_option = input()
while(temp_option != "5"):
    if (temp_option == "1"):
        puzzle = zero_up(puzzle)
        print_puzzle(puzzle)
        temp_option = input()
    if (temp_option == "2"):
        puzzle = zero_down(puzzle)
        print_puzzle(puzzle)
        temp_option = input()
    if (temp_option == "3"):
        puzzle = zero_left(puzzle)
        print_puzzle(puzzle)
        temp_option = input()
    if (temp_option == "4"):
        puzzle = zero_right(puzzle)
        print_puzzle(puzzle)
        temp_option = input()
'''