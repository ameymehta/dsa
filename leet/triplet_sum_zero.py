def threeSum(nums):
    nums.sort()
    triplets = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        pair_sums(nums, -nums[i], i+1, triplets)
    return triplets


def pair_sums(nums, target, left, triplets):
    right = len(nums)-1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            triplets.append([-target, nums[left], nums[right]])
            left += 1
            right -= 1
            while left < right and nums[left] == nums[left-1]:
                left += 1
            while left < right and nums[right] == nums[right+1]:
                right -= 1
        elif target > current_sum:
            left += 1
        else:
            right -= 1


def main():
    print(threeSum([-3, 0, 1, 2, -1, 1, -2]))
    print(threeSum([-5, 2, -1, -2, 3]))


main()
