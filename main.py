from itertools import chain

# Define the grid as a list of lists
grid = [
    [15, 3, 9, 5, 28, 46],
    [48, 31, 25, 23, 2, 50],
    [38, 19, 37, 44, 40, 20],
    [None, 1, 26, 27, 10, 43],
    [17, 6, 4, 42, 18, 16],
    [30, 39, 21, 32, None, None],
]

get_numbers = lambda cells: set(filter(lambda cell: cell is not None, cells))

find_missing_numbers = lambda cells: set(range(1, 51)) - get_numbers(cells)

missing_numbers = [[find_missing_numbers(list(chain(
    grid[row],
    [grid[i][col] for i in range(len(grid))],
    [grid[i][i] for i in range(len(grid)) if i != col and i != row],
    [grid[i][len(grid) - i - 1] for i in range(len(grid)) if i != col and i != row]
))) if grid[row][col] is None else None for col in range(len(grid[row]))] for row in range(len(grid))]

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] is None:
            print(f"Possible missing numbers for cell ({row}, {col}): {missing_numbers[row][col]}")
