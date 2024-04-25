class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memo = []
        memo.append(nums[0])
        maxProduct = nums[0]
        for i in range(1, len(nums)):
            memo.append(max(memo[i - 1] * nums[i], nums[i]))
            if memo[i] > maxProduct:
                maxProduct = memo[i]
        return maxProduct
