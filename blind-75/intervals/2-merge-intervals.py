class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        start = 0
        end = 1
        cur = intervals[0]
        result = []
        for i in range(1, len(intervals)):
            if cur[end] >= intervals[i][start]:
                cur[start] = min(cur[start], intervals[i][start])
                cur[end] = max(cur[end], intervals[i][end])
            else:
                result.append(cur)
                cur = intervals[i]
        result.append(cur)
        return result
