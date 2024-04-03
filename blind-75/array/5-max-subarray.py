class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumTracker = []
        sumTracker.append(nums[0])
        maxSum = nums[0]
        for i in range(1, len(nums)):
            iMaxSum = max(sumTracker[i-1] + nums[i], nums[i])
            sumTracker.append(iMaxSum)
            maxSum = max(maxSum, iMaxSum)
        return maxSum

def main():
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(sol.maxSubArray([1]))
    print(sol.maxSubArray([5,4,-1,7,8]))

main()