class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        result = 0
        for i in range(1, n + 1):
            result ^= i
        for num in nums:
            result ^= num
        return result
