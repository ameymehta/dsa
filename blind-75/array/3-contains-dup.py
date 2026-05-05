# https://leetcode.com/problems/contains-duplicate/description/


class Solution(object):
    def containsDuplicate(self, nums):
        m = {}
        for i in range(len(nums)):
            if nums[i] in m:
                return True
            else:
                m[nums[i]] = i
        return False
    
    def containsDuplicate_with_set(self, nums):
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False
