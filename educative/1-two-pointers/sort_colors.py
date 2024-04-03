def sort_colors(arr):
    if len(arr) <= 1:
        return arr
    
    left = 0
    right = len(arr) - 1
    current = 0

    while current <= right:
        if arr[current] == 0:
            if arr[left] != 0:
                temp = arr[current]
                arr[current] = arr[left]
                arr[left] = temp
            left += 1
            current += 1

        elif arr[current] == 1:
            current += 1
        
        elif arr[current] == 2:
            if arr[right] != 2:
                temp = arr[current]
                arr[current] = arr[right]
                arr[right] = temp
            right -= 1

    return arr
    
def main():
    inputs = [[0, 1, 0], [1, 1, 0, 2], [2, 1, 1, 0, 0], [2, 2, 2, 0, 1, 0], [2, 1, 1, 0, 1, 0, 2]]
    for i in range(len(inputs)):
        print('-----')
        print('Input for case ' + str(i))
        print(inputs[i])
        output = sort_colors(inputs[i])
        print('Output for case ' + str(i))
        print(output)


main()
