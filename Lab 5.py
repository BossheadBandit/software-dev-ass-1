def initialize_grid():
    # This function initializes a predefined 9x9 Sudoku grid with some numbers already filled in.
    # The grid is represented as a list of lists, where each inner list represents a row in the grid.
    return [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

def display_grid(grid):
    # This function takes a 9x9 Sudoku grid as input and prints it in a readable format.
    # It replaces zeros with dots to indicate empty cells.
    for row in grid:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def is_valid_move(grid, row, col, num):
    # This function checks if placing a number in a specific cell is a valid move.
    # It returns False if the number is already present in the same row.
    if num in grid[row]:
        return False
    # Additional checks for column and 3x3 subgrid should be added here.

def main():
    # This is the main function that runs the Sudoku game.
    grid = initialize_grid()  # Initialize the Sudoku grid.
    while True:
        display_grid(grid)  # Display the current state of the grid.
        try:
            # Prompt the user to enter a move in the format "row col num".
            user_input = input("Enter your move (row col num): ")
            row, col, num = map(int, user_input.split())
            if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
                if is_valid_move(grid, row, col, num):
                    grid[row][col] = num  # Place the number in the grid if the move is valid.
                else:
                    print("Invalid move. Try again.")
            else:
                print("Input out of range. Try again.")
        except ValueError:
            print("Invalid input format. Try again.")
    
    display_grid(grid)  # Display the final state of the grid.
    print("Congratulations! You completed the Sudoku puzzle.")  # Congratulate the user for completing the puzzle.

if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly.