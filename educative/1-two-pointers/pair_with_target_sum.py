def pair_with_targetsum(arr, target_sum):
    start = 0
    end = len(arr) - 1
    while start < end:
        if arr[start] + arr[end] == target_sum:
            return [start, end]
        if arr[start] + arr[end] > target_sum:
            end -= 1
        else:
            start += 1
    return [-1, -1]


def main():
    print(pair_with_targetsum([1, 2, 3, 4, 6], 6))
    print(pair_with_targetsum([2, 5, 9, 11], 11))


main()
