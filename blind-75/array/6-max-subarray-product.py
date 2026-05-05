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
    
    def maxProduct2(self, nums):
        max_prod = nums[0]
        prev_prod = nums[0]
        for i in range(1, len(nums)):
            cur_prod = max(prev_prod * nums[i], nums[i])
            prev_prod = cur_prod
            max_prod = max(cur_prod, max_prod)
        return max_prod
