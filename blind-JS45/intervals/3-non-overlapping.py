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
