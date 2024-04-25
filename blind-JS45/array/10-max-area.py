class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        max_area = 0
        if n == 0:
            return max_area
        l = 0
        r = n - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if area > max_area:
                max_area = area
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return max_area
