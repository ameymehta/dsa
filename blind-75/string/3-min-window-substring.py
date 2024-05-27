from collections import defaultdict

# Example 1:
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

# Example 2:
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.

# Example 3:
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.


class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        tMap = defaultdict(int)
        for ch in t:
            tMap[ch] += 1
        required = len(tMap)
        formed = 0

        winMap = defaultdict(int)
        winLen = -1
        winL = 0
        winR = 0
        l = 0
        for r in range(len(s)):
            ch = s[r]
            winMap[ch] += 1
            if ch in tMap and winMap[ch] == tMap[ch]:
                formed += 1
            # reducing window from left
            while l <= r and formed == required:
                lch = s[l]
                curLen = r - l + 1
                if winLen == -1 or winLen > curLen:
                    winLen = curLen
                    winL = l
                    winR = r
                winMap[lch] -= 1
                if lch in tMap and winMap[lch] < tMap[lch]:
                    formed -= 1
                l += 1

        if winLen == -1:
            return ""

        return s[winL : winR + 1]
