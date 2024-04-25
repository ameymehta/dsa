class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == "1":
                    count += 1
                    self.traverse(grid, r, c, rows, columns)
        return count

    def traverse(self, grid, r, c, rows, columns):
        if r < 0 or c < 0 or r >= rows or c >= columns or grid[r][c] != "1":
            return
        grid[r][c] = "#"
        self.traverse(grid, r + 1, c, rows, columns)
        self.traverse(grid, r - 1, c, rows, columns)
        self.traverse(grid, r, c + 1, rows, columns)
        self.traverse(grid, r, c - 1, rows, columns)
