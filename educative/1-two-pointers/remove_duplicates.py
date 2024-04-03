def remove_duplicates(arr):
    next = 1
    i = 1
    while i < len(arr):
        if arr[i-1] == arr[i]:
            arr[next] = arr[i]
            next += 1
        i += 1
    # return the next index as it is exactly
    # the number of the unique elements we have in the array
    return next


def main():
    print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
    print(remove_duplicates([2, 2, 2, 11]))


main()
