"""
https://www.finalroundai.com/blog/top-10-capital-one-code-signal-questions-you-should-prepare-for

You are given an m x n binary maze grid where:

0 represents an empty cell
1 represents a wall
You can move up, down, left, or right from and to an empty cell. Return the length of the shortest path from the top-left corner (0, 0) to the bottom-right corner (m-1, n-1). If there is no such path, return -1.

Example: For grid = [[0, 0, 1], [1, 0, 0], [1, 1, 0]]:

The output should be 5.
"""

from collections import deque

def maze_path_finder(grid):
    if not grid or not grid[0] or grid[0][0] == 1:
        return -1

    r, c = len(grid), len(grid[0])

    if grid[r-1][c-1] == 1:
        return -1

    q = deque()
    q.append((0, 0, 1))
    visited = {(0,0)}
    directions = {(0,1), (1, 0), (0, -1), (-1, 0)}

    while q:
        row, col, dist = q.popleft()

        if row == r-1 and col == c-1:
            return dist

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < r and 0 <= new_col < c and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                q.append((new_row, new_col, dist + 1))

    return -1


grid = [[0, 0, 1], [1, 0, 0], [1, 1, 0]]
maze_path_finder(grid)
