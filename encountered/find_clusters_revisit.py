class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0])
        visited = [["0" for c in range(columns)] for r in range(rows)]
        # row = [0] * columns
        # visited = row * rows
        count = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1" and visited[r][c] == "0":
                    count += 1
                    print(count)
                    self.traverse(grid, visited, rows, columns, r, c)
        return count
                    
    def traverse(self, grid, visited, rows, columns, r, c):
        visited[r][c] = "1"
        if r-1 >=0 and grid[r-1][c] == "1" and visited[r-1][c] == "0":
            self.traverse(grid, visited, rows, columns, r-1, c)
        if r+1 < rows and grid[r+1][c] == "1" and visited[r+1][c] == "0":
            self.traverse(grid, visited, rows, columns, r+1, c)
        if c-1 >= 0 and grid[r][c-1] == "1" and visited[r][c-1] == "0":
            self.traverse(grid, visited, rows, columns, r, c-1)
        if c+1 < columns and grid[r][c+1] == "1" and visited[r][c+1] == "0":
            self.traverse(grid, visited, rows, columns, r, c+1)

def find_clusters(rows, columns, grid):
    visited = [[0 for c in range(columns)] for r in range(rows)]
    num_of_clusters = 0
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == 1 and visited[r][c] == 0:
                num_of_clusters += 1
                traverse_cluster(rows, columns, grid, visited, r, c)
    return num_of_clusters
 

def traverse_cluster(rows, columns, grid, visited, r, c):
    visited[r][c] = 1
    if r+1<rows and grid[r+1][c] == 1 and visited[r+1][c] == 0:
        traverse_cluster(rows, columns, grid, visited, r+1, c)
    if c+1<columns and grid[r][c+1] == 1 and visited[r][c+1] == 0:
        traverse_cluster(rows, columns, grid, visited, r, c+1)
    if r-1>=0 and grid[r-1][c] == 1 and visited[r-1][c] == 0:
        traverse_cluster(rows, columns, grid, visited, r-1, c)
    if c-1>=0 and grid[r][c-1] == 1 and visited[r][c-1] == 0:
        traverse_cluster(rows, columns, grid, visited, r, c-1)
        


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
    # grid[0][0] = 1
    # grid[0][1] = 1
    # grid[1][0] = 1
    # grid[1][1] = 1
    # grid[2][1] = 1
    # grid[3][2] = 1
    # grid[3][3] = 1
    # grid[4][2] = 1
    # grid[4][3] = 1
    # grid[5][3] = 1

    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]

    for r in range(len(grid)):
        print(grid[r])
    sol = Solution()
    iterations = sol.numIslands(grid)
    # iterations = find_clusters(rows, columns, grid)
    print('number of iterations: ' + str(iterations))


main()
