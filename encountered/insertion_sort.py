def insertionSort2(n, arr):
    for i in range(1, n):
        current = arr[i]
        while i > 0 and arr[i-1] > current:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1
        print(arr)
    return arr


def main():
    t1 = [1, 4, 3, 5, 6, 2]
    insertionSort2(6, t1)
    t2 = [8, 7, 6, 5, 4, 3, 2, 1]
    insertionSort2(8, t2)


main()
