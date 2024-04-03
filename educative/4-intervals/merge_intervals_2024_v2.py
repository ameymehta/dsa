def merge_intervals(intervals):
    result = []
    start = 0
    end = 1
    current_start = intervals[0][start]
    current_end = intervals[0][end]
    for i in range(1, len(intervals)):
        if intervals[i][start] <= current_end:
            current_end = max(current_end, intervals[i][end])
        else:
            result.append([current_start, current_end])
            current_start = intervals[i][start]
            current_end = intervals[i][end]
    result.append([current_start, current_end])
    return result




def main():
    
    all_intervals = [
    [[1, 5], [3, 7], [4, 6]],
    [[1, 5], [4, 6], [6, 8], [11, 15]],
    [[3, 7], [6, 8], [10, 12], [11, 15]],
    [[1, 5]],
    [[1, 9], [3, 8], [4, 4]],
    [[1, 2], [3, 4], [8, 8]],
    [[1, 5], [1, 3]],
    [[1, 5], [6, 9]],
    [[0, 0], [1, 18], [1, 3]]
    ]

    for i in range(len(all_intervals)):
        print('---')
        print(str(i + 1) + '. Input: ' + str(all_intervals[i]))
        print(str(i + 1) + '. Result ' + str(merge_intervals(all_intervals[i])))

main()