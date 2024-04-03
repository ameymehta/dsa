def binary_search(nums, target):
    low = 0
    high = len(nums)-1
    while low <= high:
        mid = low + ((high-low)//2)
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def main():
    nums_lists = [
        [], 
        [0, 1],
        [1, 2, 3], 
        [-1, 0, 3, 5, 9, 12], 
        [-100, -67, -55, -50, -49, -40, -33, -22, -10, -5]
      ]
    target_list = [12, 1, 3, 9, -22]

    for i in range(len(nums_lists)):
        nums = nums_lists[i]
        target = target_list[i]
        index = binary_search(nums, target)

        print(i+1, ".\tArray to search: ", nums, sep="")
        print("\tTarget: ", target, sep="")

        if index != -1:
            print("\t", target, " exists in the array at index ", index, sep="")
        else:
            print("\t", target, " does not exist in the array so the return value is ", index, sep="")
        print('-' * 100)


if __name__ == '__main__':
		main()
