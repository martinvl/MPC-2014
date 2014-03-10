# @EXPECTED_RESULT@: CORRECT

from sys import stdin

# This solution uses dynamic programming.

# Input
T = int(stdin.readline())
for tc in range(T):
    l = stdin.readline().split()
    X = int(l[0])
    Y = int(l[1])
    M = int(l[2])

    # Initialize grid
    grid = [[0]*Y for i in range(X)]

    # Input vertical walls
    vertical_walls = []
    for i in range(X):
        l = stdin.readline().split()
        vertical_walls.append([int(k) for k in l])

    # Input horizontal walls
    horizontal_walls = []
    for i in range(X-1):
        l = stdin.readline().split()
        horizontal_walls.append([int(k) for k in l])

    # Init first row and first col
    grid[0][0] = M
    for i in range(1, X):
        grid[i][0] = grid[i-1][0]
        if horizontal_walls[i-1][0] == 1:
            grid[i][0] -= 1

    for i in range(1, Y):
        grid[0][i] = grid[0][i-1]
        if vertical_walls[0][i-1] == 1:
            grid[0][i] -= 1

    # Use DP on the remiander of the grid
    for i in range(1, X):
        for j in range(1, Y):
            from_x = grid[i-1][j]
            if horizontal_walls[i-1][j] == 1:
                from_x -= 1
            from_y = grid[i][j-1]
            if vertical_walls[i][j-1] == 1:
                from_y -= 1
            grid[i][j] = max(from_x, from_y)

    print max(0, grid[X-1][Y-1])
