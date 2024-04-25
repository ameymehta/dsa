class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n == 0:
            return 0

        nums.sort()

        count = 1
        max_count = 0

        for i in range(1, n):
            if nums[i] != nums[i - 1]:
                if nums[i] == nums[i - 1] + 1:
                    count += 1
                else:
                    max_count = max(max_count, count)
                    count = 1
        max_count = max(max_count, count)
        return max_count
