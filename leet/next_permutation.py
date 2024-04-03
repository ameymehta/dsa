def nextPermutation(nums):
    # Find first number from back of array that is lesser than next number on array
    # 9,8,4,7,6,5,1
    # i = 2 is less than i = 3 that is 4 is less than 7
    i = len(nums) - 2
    while i >= 0:
        if nums[i] < nums[i+1]:
            break
        i -= 1

    # Find number than is next highest to i th number and swap them
    # Swap i = 2 with j = 5, that is swap 4 and 5
    # 9,8,5,7,6,4,1
    if i >= 0:
        j = i + 1
        while j <= len(nums) - 1:
            if nums[j] <= nums[i]:
                break
            j += 1
        j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        # Reverse all the numbers on right of i and return the resultant array
        # Return 9,8,5,1,4,6,7
        return reversePerm(nums, i+1, len(nums) - 1)
    else:
        # Reverse complete array for all descending numbers input 5,4,3,2,1
        return reversePerm(nums, 0, len(nums) - 1)


def reversePerm(nums, start, end):
    while(start <= end):
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
    return nums


def main():
    print(nextPermutation([1, 2, 3]))
    print(nextPermutation([1, 3, 2]))
    print(nextPermutation([5, 1, 1]))
    print(nextPermutation([6, 3, 1]))
    print(nextPermutation([9, 8, 4, 7, 6, 5, 1]))


main()
