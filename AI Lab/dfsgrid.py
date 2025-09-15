from collections import deque

# 0 = free cell, 1 = obstacle
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

rows = len(grid)
cols = len(grid[0])

start = (0, 0)  # Top-left corner
goal = (3, 3)   # Bottom-right corner

# Moves: up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid(x, y, visited):
    return 0 <= x < rows and 0 <= y < cols and grid[x][y] == 0 and not visited[x][y]

def dfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    stack = [(start, [start])]
    visited[start[0]][start[1]] = True

    while stack:
        (x, y), path = stack.pop()
        if (x, y) == goal:
            return path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny, visited):
                visited[nx][ny] = True
                stack.append(((nx, ny), path + [(nx, ny)]))
    return None

def print_grid_with_path(path, title):
    print(f"\n{title}")
    for i in range(rows):
        for j in range(cols):
            if (i, j) == start:
                print("S", end=" ")
            elif (i, j) == goal:
                print("G", end=" ")
            elif path and (i, j) in path:
                print("*", end=" ")
            elif grid[i][j] == 1:
                print("]", end=" ")
            else:
                print(".", end=" ")
        print()

# Print initial grid
print("\nInitial Grid:")
for row in grid:
    print(" ".join(str(cell) for cell in row))

# Run DFS
dfs_path = dfs(grid, start, goal)

if dfs_path:
    print("\nDFS Path Found:", dfs_path)
    print_grid_with_path(dfs_path, "DFS Path in Grid:")
else:
    print("\nDFS:")