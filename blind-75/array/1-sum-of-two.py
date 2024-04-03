class Solution(object):
    def twoSum(self, nums, target):
        visited = {}
        for i in range(len(nums)):
            pairValue = target - nums[i]
            if pairValue in visited:
                pairIndex = visited[pairValue]
                return [pairIndex, i]
            visited[nums[i]] = i
        return [-1, -1]

def main():
    solution = Solution()
    inputs = [[2,7,11,15], [2,9,4,11,6,7]]
    targets = [9, 16]
    for i in range(len(targets)):
        print(solution.twoSum(inputs[i], targets[i]))

main()
