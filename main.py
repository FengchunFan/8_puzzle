# will build the project based on x, y coordinates
# operators will be based on how 0 moves, thus 4 possible options

# this following puzzle will be used for default goal state
# [[1, 2, 3]]    [[(0,0), (0,1), (0,2)]]
# [[4, 5, 6]] == [[(1,0), (1,1), (1,2)]]
# [[7, 8, 0]]    [[(2,0), (2,1), (2,2)]]

# default 3 x 3 puzzle
def print_puzzle(puzzle):
    print("This will be your starting puzzle: ")
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
    print()

def zero_up(puzzle):
    print()

def zero_down(puzzle):
    print()

def zero_left(puzzle):
    print()

def zero_right(puzzle):
    print()

# Uniform Cost Search
def algo_1(puzzle):
    print("You have chosen the Uniform Cost Search algorithm")

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
    puzzle = [[1, 2, 3],[4, 8, 0],[7, 6, 5]]
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