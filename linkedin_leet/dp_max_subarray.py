class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = []
        memo.append(nums[0])
        maxSum = nums[0]
        for i in range(1, len(nums)):
            memo.append(max(memo[i-1] + nums[i], nums[i]))
            if memo[i] > maxSum:
                maxSum = memo[i]
        return maxSum