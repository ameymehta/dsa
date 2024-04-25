class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # recursion/dfs
        # return self.dfs(0, 0, text1, text2)

        # memoization
        l1 = len(text1)
        l2 = len(text2)
        dp = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]
        result = 0
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
                result = max(result, dp[i][j])
        return result

    def dfs(self, p1, p2, text1, text2):
        if p1 == len(text1) or p2 == len(text2):
            return 0

        if text1[p1] == text2[p2]:
            return 1 + self.dfs(p1 + 1, p2 + 1, text1, text2)
        else:
            return max(
                self.dfs(p1 + 1, p2, text1, text2), self.dfs(p1, p2 + 1, text1, text2)
            )
