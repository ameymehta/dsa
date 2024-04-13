class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)
            print("i: " + str(i) + ", res: " + str(result[i]))
        return result
