# Original
# [1,2,3]
# [4,5,6]
# [7,8,9]

# reverse the rows (flip horizontally)
# [7,8,9]
# [4,5,6]
# [1,2,3]

# transpose (flip diagnolly)
# [7,4,1]
# [8,5,2]
# [9,6,3]


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # reverse the rows (flip horizontally)
        l = 0
        r = len(matrix) - 1
        while l < r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1
            r -= 1

        # transpose (flip diagnolly)
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
