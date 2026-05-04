def flip(arr, i):
    l = 0
    r = i
    while l < r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1
    return arr

def find_max(arr, n):
    max_i = 0
    for i in range(1, n):
        if arr[i] > arr[max_i]:
            max_i = i
    return max_i

def pancake_sort(arr):
    n = len(arr)
    cur_size = n
    while cur_size > 1:
        max_i = find_max(arr, cur_size)
        # check if max_i is not the end index already, in that case no need to perform flips
        if max_i != cur_size-1:
            # move the max number to the begining by first flip (sub array is till max index)
            flip(arr, max_i)
            # now move the max number to the end by second flip (sub array is till the end of unsorted part i.e. cur_size-1)
            flip(arr, cur_size-1)
        cur_size -= 1
    return arr

print(str(pancake_sort([1,5,4,3,2])))
print(str(pancake_sort([10, 23, 54, 71, 2, 13])))
