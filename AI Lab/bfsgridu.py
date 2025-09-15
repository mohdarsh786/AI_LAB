from collections import deque
def bfs(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start, [start])])
    visited[start[0]][start[1]] = True

    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append(((nx, ny), path + [(nx, ny)]))
    return None

m = int(input("Enter number of rows (m): "))
n = int(input("Enter number of columns (n): "))

print("Enter the grid row by row (0 for open, 1 for obstacle):")
grid = []
for i in range(m):
    row = list(map(int, input(f"Row {i+1}: ").strip().split()))
    if len(row) != n:
        print("Invalid row length. Please enter exactly", n, "values.")
        exit(1)
    grid.append(row)

start = (0, 0)
goal = (m-1, n-1)

path = bfs(grid, start, goal)

if path:
    print("\nShortest path found:")
    print(path)
else:
    print("\nNo path found from", start, "to", goal)
    