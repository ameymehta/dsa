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