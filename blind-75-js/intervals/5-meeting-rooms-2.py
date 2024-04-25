# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: 1


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        events = []
        start = 0
        end = 1
        for interval in intervals:
            events.append([interval[start], 1])
            events.append([interval[end], -1])

        events.sort()

        rooms = 0
        max_rooms = 0
        for event in events:
            rooms += event[1]
            if rooms > max_rooms:
                max_rooms = rooms

        return max_rooms
