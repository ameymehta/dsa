class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        n = len(nums)
        if n == 0:
            return result
        nums.sort()
        for i in range(n):
            l = i + 1
            r = n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    result.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1
        return result