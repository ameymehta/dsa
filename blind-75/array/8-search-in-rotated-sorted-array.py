class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # for i in range(len(nums)):
        #     if nums[i] == target:
        #         return i
        # return -1
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[l] <= target and nums[mid] >= target:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[r] >= target and nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1
