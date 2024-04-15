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
        t_dict = defaultdict(int)
        for c in t:
            t_dict[c] += 1

        required = len(t_dict)
        formed = 0
        l = 0
        window_dict = defaultdict(int)
        res_len = -1
        res_l = 0
        res_r = 0

        for r in range(len(s)):
            c = s[r]
            window_dict[c] += 1

            if c in t_dict and window_dict[c] == t_dict[c]:
                formed += 1

            while l <= r and formed == required:
                c = s[l]

                if res_len == -1 or r - l + 1 < res_len:
                    res_len = r - l + 1
                    res_l = l
                    res_r = r

                window_dict[c] -= 1

                if c in t_dict and window_dict[c] < t_dict[c]:
                    formed -= 1

                l += 1

        if res_len == -1:
            return ""

        return s[res_l : res_r + 1]
