#will build the project based on x, y coordinates
#operators will be based on how 0 moves, thus 4 possible options

#default 3 x 3 puzzle
def print_puzzle(puzzle):
    for i in range(3):
        for j in range(3):
            print(puzzle[i][j], end = " ") #use end = " " to prevent duplicated newlines
        print() #newline

print("Welcome to the 8 puzzle solver")
print("Type “1” to use a default puzzle, or “2” to enter your own puzzle")

puzzle_option = input()
puzzle = []

while(puzzle_option != "1" and puzzle_option != "2"):
    print("Please enter a valid option")
    puzzle_option = input()

if(puzzle_option == "1"):
    print("Here is a default puzzle")
    puzzle = [[1, 2, 3],[4, 8, 0],[7, 6, 5]]
    print_puzzle(puzzle)
    
elif(puzzle_option == "2"):
    print("Enter your puzzle, use a zero to represent the blank")
