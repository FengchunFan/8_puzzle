# will build the project based on x, y coordinates
# operators will be based on how 0 moves, thus 4 possible options

# this following puzzle will be used for default goal state
# [[1, 2, 3]]    [[(0,0), (0,1), (0,2)]]
# [[4, 5, 6]] == [[(1,0), (1,1), (1,2)]]
# [[7, 8, 0]]    [[(2,0), (2,1), (2,2)]]

from queue import PriorityQueue #essential for algorithms
import copy

# define a Node class to keep track of path used, should have a type puzzle and a puzzle pointer
class Node:
    def __init__(self, puzzle, parent, cost):
        self.puzzle = puzzle
        self.parent = parent
        self.cost = cost

    def __lt__(self, other): # very very important, used for comparison for the priority queue, lower cost = higher priority
        return self.cost < other.cost

# default 3 x 3 puzzle
def print_puzzle(puzzle):
    for i in range(3):
        for j in range(3):
            print(puzzle[i][j], end = " ") #use end = " " to prevent duplicated newlines
        print() #newline

def get_row(row_input):
    row = []
    for index in row_input:
        if index.isdigit():
            row.append(index)
    return row

# 4 operators up, down, left, right. But all requires to know 0's position first

def find_zero(puzzle):
    for i in range (3):
        for j in range (3):
            if puzzle[i][j] == '0':
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

# Uniform Cost Search
# reference: https://www.geeksforgeeks.org/priority-queue-using-queue-and-heapdict-module-in-python/
def algo_1(puzzle):
    print("You have chosen the Uniform Cost Search algorithm")
    goal = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '0']] #set the goal state
    start_node = Node(puzzle, None, 0) #use the input puzzle to initialize the start node
    q = PriorityQueue()  #create priority queue
    q.put(start_node) #add start_node to the start of the priority queue
    visited_node = [] #add a array to store visited nodes

    while not q.empty(): 
        temp_node = q.get() #get the first node off priority queue
        temp_puzzle = temp_node.puzzle #get the puzzle from the node at starting of priority queue
        #print_puzzle(temp_puzzle)
        if(puzzle == goal): #check if is goal
            print("Goal state was reached")
            return None #break out of the loop
        possible_moves = [zero_up(temp_puzzle), zero_down(temp_puzzle), zero_left(temp_puzzle), zero_right(temp_puzzle)] #4 operators
        for moves in possible_moves:
            if moves != temp_puzzle: #if there is update in the puzzle, i.e: move is valid
                if moves not in visited_node:
                    curr_node = Node(moves, temp_puzzle, temp_node.cost + 1)
                    q.put(curr_node)
                    visited_node.append(moves)

    print("Goal state could not be reached.") #end of the queue has been reached and still not found goal state

# A* with the Misplaced Tile heuristic
def algo_2(puzzle):
    print("You have chosen the A* with the Misplaced Tile heuristic algorithm")

# A* with the Euclidean distance heuristic
def algo_3(puzzle):
    print("You have chosen the A* with the Euclidean distance heuristic algorithm")

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