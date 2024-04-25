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
        freq = {}
        for i in range(n):
            if s[i] not in freq:
                freq[s[i]] = 0
            freq[s[i]] += 1
            if t[i] not in freq:
                freq[t[i]] = 0
            freq[t[i]] -= 1

        for k in freq:
            if freq[k] != 0:
                return False

        return True
