# There is a robot on an m x n grid.
# The robot is initially located at the top-left corner (i.e., grid[0][0]).
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# Example 1:
# Input: m = 3, n = 7
# Output: 28

# Example 2:
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Purpose: find # ways to go from top-left to bottom-right
        # Formula: res[i][j] += res[all i][j - 1]
        # instead of using 2d res/dp array, here 1d is used, its overridden with each iteration of i loop
        # build
        dp = [0] * n
        dp[0] = 1

        # find
        for i in range(m):
            for j in range(n):
                if j >= 1:
                    dp[j] += dp[j - 1]

        # return
        return dp[-1]
