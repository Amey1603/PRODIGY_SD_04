# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

# Function to check if placing `num` in grid[row][col] is valid
def is_valid(grid, row, col, num):
    # Check if `num` is in the row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check if `num` is in the column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check if `num` is in the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True

# Backtracking function to solve the Sudoku
def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            # Look for an empty cell (represented by 0)
            if grid[row][col] == 0:
                # Try placing numbers 1-9
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num  # Place the number
                        if solve_sudoku(grid):  # Recur with this placement
                            return True
                        grid[row][col] = 0  # Backtrack if needed
                return False  # Trigger backtracking if no number works
    return True  # Puzzle solved

# Example Sudoku puzzle (0 represents empty cells)
sudoku_grid = [
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

# Solve and display the result
if solve_sudoku(sudoku_grid):
    print("Sudoku puzzle solved successfully!")
    print_grid(sudoku_grid)
else:
    print("No solution exists for the given Sudoku puzzle.")
