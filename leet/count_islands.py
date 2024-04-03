def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    rows = len(grid)
    if rows == 0:
        return 0
    cols = len(grid[0])
    if cols == 0:
        return 0
    visited = [[0 for c in range(cols)] for r in range(rows)]
    island_count = 0
    for r in range(rows):
        for c in range(cols):
            if int(grid[r][c]) == 1 and visited[r][c] == 0:
                island_count += 1
                traverse_island(grid, visited, r, c, rows, cols)
    return island_count


def traverse_island(grid, visited, r, c, rows, cols):
    if int(grid[r][c]) == 0 or visited[r][c] == 1:
        return False

    visited[r][c] = 1

    if r-1 >= 0:
        traverse_island(grid, visited, r-1, c, rows, cols)
    if c-1 >= 0:
        traverse_island(grid, visited, r, c-1, rows, cols)
    if r+1 < rows:
        traverse_island(grid, visited, r+1, c, rows, cols)
    if c+1 < cols:
        traverse_island(grid, visited, r, c+1, rows, cols)


def main():
    grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"],
            ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
    print(numIslands(grid))


main()
