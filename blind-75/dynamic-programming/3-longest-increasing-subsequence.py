from bisect import bisect_left


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # memo = [0] * len(nums)
        # max_size = 0
        # for num in nums:
        #     print(num)
        #     i = 0
        #     j = max_size
        #     while i != j:
        #         mid = (i + j) / 2
        #         if memo[mid] < num:
        #             i = mid + 1
        #         else:
        #             j = mid
        #     memo[i] = num
        #     max_size = max(i + 1, max_size)
        #     print(memo)
        # return max_size

        arr = [nums.pop(0)]
        for num in nums:
            if num > arr[-1]:
                arr.append(num)
            else:
                # determine the furthest position in arr at which num could be placed
                # so that arr remains strictly increasing, and overwrite the element at that position in arr with num.
                arr[bisect_left(arr, num)] = num
        return len(arr)
