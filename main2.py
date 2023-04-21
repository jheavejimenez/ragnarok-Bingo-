# Define the grid as a list of lists
grid = [
    [15, 3, 9, 5, 28, 46],
    [48, 31, 25, 23, 2, 50],
    [38, 19, 37, 44, 40, 20],
    [None, 1, 26, 27, 10, 43],
    [17, 6, 4, 42, 18, 16],
    [30, 39, 21, 32, None, None],
]


def get_numbers(cells):
    return set(cell for cell in cells if cell is not None)


def find_missing_numbers(cells):
    present_numbers = get_numbers(cells)
    return set(range(1, 51)) - present_numbers


for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] is None:
            row_numbers = grid[row]
            col_numbers = [grid[i][col] for i in range(len(grid))]
            diagonal1_numbers = [grid[i][i] for i in range(len(grid)) if i != col and i != row]
            diagonal2_numbers = [grid[i][len(grid) - i - 1] for i in range(len(grid)) if i != col and i != row]
            possible_numbers = find_missing_numbers(row_numbers + col_numbers + diagonal1_numbers + diagonal2_numbers)
            print(f"Possible missing numbers for cell ({row}, {col}): {possible_numbers}")
