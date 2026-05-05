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
    
    def productExceptSelf2(self, nums):
        product_of_all = 1
        zero_count = 0
        result = [0 for _ in range(len(nums))]
        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product_of_all *= num
        if zero_count > 1:
            return result
        for i in range(len(nums)):
            if zero_count == 1:
                if nums[i] == 0:
                    result[i] = product_of_all
                    return result
                else:
                    continue           
            result[i] = product_of_all/nums[i]
        
        return result


def main():
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))
    print(sol.productExceptSelf([-1, 1, 0, -3, 3]))


main()
