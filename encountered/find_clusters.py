def find_cluster(rows, columns, grid):
    visited = [[0 for c in range(columns)] for r in range(rows)]
    cluster_count = 0
    for r in range(rows):
        for c in range(columns):
            if(grid[r][c] == 1 and visited[r][c] == 0):
                cluster_count += 1
                traverse_cluster(r, c, visited, rows, columns, grid)
    return cluster_count


def traverse_cluster(r, c, visited, rows, columns, grid):
    visited[r][c] = 1
    if r - 1 >= 0 and grid[r - 1][c] == 1 and visited[r - 1][c] == 0:
        traverse_cluster(r - 1, c, visited, rows, columns, grid)

    if c - 1 >= 0 and grid[r][c - 1] == 1 and visited[r][c - 1] == 0:
        traverse_cluster(r, c - 1, visited, rows, columns, grid)

    if r + 1 < rows and grid[r + 1][c] == 1 and visited[r + 1][c] == 0:
        traverse_cluster(r + 1, c, visited, rows, columns, grid)

    if c + 1 < columns and grid[r][c + 1] == 1 and visited[r][c + 1] == 0:
        traverse_cluster(r, c + 1, visited, rows, columns, grid)


def main():
    rows = 7
    columns = 7
    grid = [[0 for c in range(columns)] for r in range(rows)]

    # 2 cluster
    # grid[0][0] = 1
    # grid[0][1] = 1
    # grid[1][0] = 1
    # grid[1][1] = 1
    # grid[2][1] = 1
    # grid[4][5] = 1
    # grid[3][5] = 1
    # grid[4][4] = 1
    # grid[3][4] = 1

    # diagonal 1s
    # grid[0][0] = 1
    # grid[1][1] = 1
    # grid[2][2] = 1
    # grid[3][3] = 1
    # grid[4][4] = 1
    # grid[5][5] = 1
    # grid[6][6] = 1

    # 2 close clusters
    grid[0][0] = 1
    grid[0][1] = 1
    grid[1][0] = 1
    grid[1][1] = 1
    grid[2][1] = 1
    grid[3][2] = 1
    grid[3][3] = 1
    grid[4][2] = 1
    grid[4][3] = 1
    grid[5][3] = 1

    for r in range(rows):
        print(grid[r])
    iterations = find_cluster(rows, columns, grid)
    print('number of iterations: ' + str(iterations))


main()
