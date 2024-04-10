class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        productOfAll = 1
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
            else:
                productOfAll = productOfAll * num

        answer = []
        if zeroCount > 1:
            return [0] * len(nums)

        for num in nums:
            if num != 0:
                if zeroCount == 1:
                    answer.append(0)
                else:
                    answer.append(productOfAll // num)
            else:
                answer.append(productOfAll)

        return answer


def main():
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))
    print(sol.productExceptSelf([-1, 1, 0, -3, 3]))


main()
