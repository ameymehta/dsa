class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + ((right - left)//2)

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[right]
        # return nums[left] # works too
    
def main():
    sol = Solution()
    print(sol.findMin([3,4,5,1,2]))
    print(sol.findMin([4,5,6,7,0,1,2]))
    print(sol.findMin([11,13,15,17]))


main()