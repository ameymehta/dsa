class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        if not matrix or not matrix[0]:
            return result
        rows = len(matrix)
        columns = len(matrix[0])
        left = 0
        right = columns - 1
        top = 0
        bottom = rows - 1
        while left <= right and top <= bottom:
            # traverse right
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1
            # traverse down
            for r in range(top, bottom + 1):
                result.append(matrix[r][right])
            right -= 1
            # traverse left
            if top <= bottom:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1
            # traverse up:
            if left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1
        return result
