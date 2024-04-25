class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        columns = len(matrix[0])

        zeros_rows = [False] * rows
        zeros_columns = [False] * columns

        for r in range(rows):
            for c in range(columns):
                if matrix[r][c] == 0:
                    zeros_rows[r] = True
                    zeros_columns[c] = True

        for r in range(rows):
            for c in range(columns):
                if zeros_rows[r] or zeros_columns[c]:
                    matrix[r][c] = 0
