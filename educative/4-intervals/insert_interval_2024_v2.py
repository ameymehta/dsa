def insert_interval(intervals,new_interval):
    start = 0
    end = 1
    i = 0
    result = []
    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        result.append(intervals[i])
        i += 1
    while i < len(intervals) and intervals[i][end] < new_interval[end]:
        new_interval[start] = min(new_interval[start], intervals[i][start])
        new_interval[end] = max(new_interval[end], intervals[i][end])
        i += 1
    result.append(new_interval)
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    return result



def main():
    new_interval = [[5, 7], [8, 9], [10, 12], [1, 3], [1, 10]]
    existing_intervals = [
        [[1, 2], [3, 5], [6, 8]],
        [[1, 3], [5, 7], [10, 12]],
        [[8, 10], [12, 15]],
        [[5, 7], [8, 9]],
        [[3, 5]]
    ]
    for i in range(len(new_interval)):
        print('---')
        print(str(i + 1) + '. Input: ' + str(new_interval[i]) + ' and ' + str(existing_intervals[i]))
        print(str(i + 1) + '. Result ' + str(insert_interval(existing_intervals[i],new_interval[i])))

main()
