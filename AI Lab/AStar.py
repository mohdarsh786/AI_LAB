import heapq
import math

ROW = COL= 10

def is_valid(row, col, grid):
    return (0 <= row < ROW) and (0 <= col < COL) and grid[row][col] == 1

def trace_path(parent, dest):
    print("The Path is ")
    row, col = dest
    path = []
    while parent[row][col] != (row, col):
        path.append((row, col))
        row, col = parent[row][col]
    path.append((row, col))
    path.reverse()
    for i in path:
        print("->", i, end=" ")
    print()

def a_star(grid, src, dest):
    if not is_valid(src[0], src[1], grid) or not is_valid(dest[0], dest[1], grid):
        print("Source or destination is invalid or blocked")
        return

    if src == dest:
        print("We are already at the destination")
        return

    closed_list = [[False for _ in range(COL)] for _ in range(ROW)]
    parent = [[(i, j) for j in range(COL)] for i in range(ROW)]
    f = [[float('inf') for _ in range(COL)] for _ in range(ROW)]
    g = [[float('inf') for _ in range(COL)] for _ in range(ROW)]

    i, j = src
    f[i][j] = 0
    g[i][j] = 0
    parent[i][j] = (i, j)

    open_list = []
    heapq.heappush(open_list, (0.0, i, j))
    found_dest = False

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    while open_list:
        _, i, j = heapq.heappop(open_list)
        closed_list[i][j] = True

        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            if is_valid(ni, nj, grid) and not closed_list[ni][nj]:
                if (ni, nj) == tuple(dest):
                    parent[ni][nj] = (i, j)
                    print("The destination cell is found")
                    trace_path(parent, dest)
                    return
                g_new = g[i][j] + 1.0
                h_new = math.hypot(ni - dest[0], nj - dest[1])
                f_new = g_new + h_new
                if f[ni][nj] == float('inf') or f[ni][nj] > f_new:
                    heapq.heappush(open_list, (f_new, ni, nj))
                    f[ni][nj] = f_new
                    g[ni][nj] = g_new
                    parent[ni][nj] = (i, j)
    print("Failed to find the destination cell")

def main():
    grid = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 0, 1]
    ]
    src = [8, 0]
    dest = [0, 0]
    a_star(grid, src, dest)

if __name__ == "__main__":
    main()