import heapq
from collections import defaultdict


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        h = []
        m = defaultdict(int)
        result = []
        for num in nums:
            m[num] += 1
        for key in m:
            # to make default heap, max heap, add counts in negative
            heapq.heappush(h, (-m[key], key))
        for i in range(k):
            result.append(heapq.heappop(h)[1])
        return result
