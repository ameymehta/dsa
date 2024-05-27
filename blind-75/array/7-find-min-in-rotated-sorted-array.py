class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[r]
        # return nums[l] works as well


def main():
    sol = Solution()
    print(sol.findMin([3, 4, 5, 1, 2]))
    print(sol.findMin([4, 5, 6, 7, 0, 1, 2]))
    print(sol.findMin([11, 13, 15, 17]))


main()
