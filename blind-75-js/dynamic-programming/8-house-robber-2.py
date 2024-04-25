# You can't rob 2 neighboring houses
# All houses are in circle
# So, 1st in the array and last in the array are neighbors

# Example 1:
# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

# Example 2:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

# Example 3:
# Input: nums = [1,2,3]
# Output: 3


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp1, dp2 = [0] * n, [0] * n

        dp1[0] = nums[0]
        dp1[1] = nums[0]
        dp2[0] = 0
        dp2[1] = nums[1]

        for i in range(2, n):
            dp1[i] = max(nums[i] + dp1[i - 2], dp1[i - 1])
            dp2[i] = max(nums[i] + dp2[i - 2], dp2[i - 1])

        return max(dp1[n - 2], dp2[n - 1])
