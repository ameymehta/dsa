# leet 217. https://leetcode.com/problems/contains-duplicate-ii/description/


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m = {}
        for i in range(len(nums)):
            if nums[i] in m and abs(m[nums[i]] - i) <= k:
                return True
            # in case if num[i] in map and distance not <= k, add the new index
            else:
                m[nums[i]] = i
        return False
