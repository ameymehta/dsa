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
        cur = intervals[0]
        for i in range(1, len(intervals)):
            if cur[end] > intervals[i][start]:
                # overlapping found, count it
                result += 1
                if intervals[i][end] < cur[end]:
                    cur[end] = intervals[i][end]
            else:
                cur[end] = intervals[i][end]

        return result
