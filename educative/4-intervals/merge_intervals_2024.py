def merge_intervals(intervals):
    result = []
    start = intervals[0][0]
    end = intervals[0][1]

    for i in range(1, len(intervals)):
        interval_start = intervals[i][0]
        interval_end = intervals[i][1]
        if interval_start <= end:
            end = max(end, interval_end)
        else:
            result.append([start, end])
            start = interval_start
            end = interval_end
    
    result.append([start, end])
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
