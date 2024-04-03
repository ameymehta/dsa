def make_squares(arr):
    left = 0
    right = len(arr) - 1
    highest_index = right
    squares = [0 for i in range(right + 1)]
    while left <= right:
        left_sq = arr[left] * arr[left]
        right_sq = arr[right] * arr[right]
        if left_sq <= right_sq:
            squares[highest_index] = right_sq
            right -= 1
        else:
            squares[highest_index] = left_sq
            left += 1
        highest_index -= 1
    return squares


def main():

    print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
    print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))


main()
