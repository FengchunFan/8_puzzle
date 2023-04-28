#will build the project based on x, y coordinates
#operators will be based on how 0 moves, thus 4 possible options

#default 3 x 3 puzzle
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

print("Welcome to the 8 puzzle solver")
print("Type “1” to use a default puzzle, or “2” to enter your own puzzle")

puzzle_option = input()
puzzle = []

while(puzzle_option != "1" and puzzle_option != "2"):
    print("Please enter a valid option")
    puzzle_option = input()

if(puzzle_option == "1"):
    #default
    print("Here is a default puzzle")
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

#up to this point, the initial puzzle should be formed