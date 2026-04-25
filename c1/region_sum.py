"""
https://www.finalroundai.com/blog/top-10-capital-one-code-signal-questions-you-should-prepare-for

Given a 2D matrix matrix, handle multiple queries of the following type:

Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Implement the NumMatrix class:

NumMatrix(int[][] matrix) initializes the object with the integer matrix.
int sumRegion(int row1, int col1, int row2, int col2) returns the sum of the elements of matrix inside the rectangle.
Example for matrix
[[3, 0, 1, 4, 2], 
 [5, 6, 3, 2, 1], 
 [1, 2, 0, 1, 5], 
 [4, 1, 0, 1, 7], 
 [1, 0, 3, 0, 5]]

region_sum(matrix, (2, 1, 4, 3)) should return 8
region_sum(matrix, (1, 1, 2, 2)) should return 11
"""


from collections import deque

def region_sum(grid, tup):
    topleft = (tup[0], tup[1])
    botright = (tup[2], tup[3])
    r = len(grid)
    c = len(grid[0])
    if topleft[0] < 0 or topleft[1] < 0 or botright[0] > r - 1 or botright[1] > c - 1:
        return -1

    # BFS setup
    q = deque()
    q.append(topleft)
    visited = {topleft}
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

    sum = 0

    while q:
        row, col = q.popleft()
        sum += grid[row][col]

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if topleft[0] <= new_row <= botright[0] and topleft[1] <= new_col <= botright[1] and (new_row, new_col) not in visited:
                visited.add((new_row, new_col))
                q.append((new_row, new_col))

    return sum


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
print(region_sum(matrix, (2, 1, 4, 3)))  # Output: 8
print(region_sum(matrix, (1, 1, 2, 2)))  # Output: 11