# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        n = len(s)
        m = defaultdict(int)
        for i in range(n):
            m[s[i]] += 1
            m[t[i]] -= 1
        for key in m:
            if m[key] != 0:
                return False
        return True
