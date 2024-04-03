class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        memo = [[0 for i in range(n+1)] for j in range(m+1)]
        
        for i in range(1, m+1):
            memo[i][0] = i
        for j in range(1, n+1):
            memo[0][j] = j
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    memo[i][j] = memo[i-1][j-1]
                else:
                    memo[i][j] = min(memo[i-1][j-1], memo[i][j-1], memo[i-1][j]) + 1
            
        return memo[m][n]