class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        if not heights or not heights[0]:
            return heights
        rows = len(heights)
        columns = len(heights[0])
        visited_pacific = set()
        visited_atlantic = set()

        # Approach is to start from both sides of
        # the oceans and then reach each point that can be
        # reached while maintaining the visited indices

        # Iterate over columns and start from both 0, rows-1 rows
        for c in range(columns):
            # first row
            self.dfs(visited_pacific, 0, c, heights[0][c], heights)
            # last row
            self.dfs(visited_atlantic, rows - 1, c, heights[rows - 1][c], heights)

        # Iterate over rows and start from both 0, columns-1 cols
        for r in range(rows):
            # first column
            self.dfs(visited_pacific, r, 0, heights[r][0], heights)
            # last column
            self.dfs(visited_atlantic, r, columns - 1, heights[r][columns - 1], heights)

        # Co-ordinates which can reach both the oceans are the winners
        # so we take intersection
        result = visited_atlantic.intersection(visited_pacific)

        return result

    def dfs(self, visited_set, r, c, cur_height, heights):
        if (
            r < 0
            or r >= len(heights)
            or c < 0
            or c >= len(heights[0])
            or (r, c) in visited_set
            or cur_height > heights[r][c]
        ):
            return

        visited_set.add((r, c))

        cur_height = heights[r][c]
        self.dfs(visited_set, r + 1, c, cur_height, heights)
        self.dfs(visited_set, r - 1, c, cur_height, heights)
        self.dfs(visited_set, r, c + 1, cur_height, heights)
        self.dfs(visited_set, r, c - 1, cur_height, heights)
