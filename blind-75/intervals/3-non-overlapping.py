# how many intervals you will have to remove to make rest non-overlaping
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        result = 0
        start = 0
        end = 1
        cur_end = intervals[0][end]
        for i in range(1, len(intervals)):
            # if overlapping, count it and adjust cur_end
            if cur_end > intervals[i][start]:
                result += 1
                if intervals[i][end] < cur_end:
                    cur_end = intervals[i][end]
            # if not overlapping, update cur_end
            else:
                cur_end = intervals[i][end]

        return result

    def eraseOverlapIntervals2(self, intervals):
        start = 0
        end = 1
        result = 0
        intervals.sort(key=lambda x:x[0])
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if cur[end] < intervals[i][start]:
                # result.append(cur)
                cur = intervals[i]
            # elif cur[start] <= intervals[i][end]:
            elif cur[end] > intervals[i][start]:
                result += 1
                # cur[start] = min(cur[start], intervals[i][start])
                # cur[end] = max(cur[end], intervals[i][end])
                cur[end] = min(cur[end], intervals[i][end])
            else:
                # result.append(cur)
                cur = intervals[i]
        # result.append(cur)
        return result