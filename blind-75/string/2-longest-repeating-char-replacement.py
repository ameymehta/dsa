# Example 1:
# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

# Example 2:
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.


class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        m = defaultdict(int)
        l = 0
        maxLen = 0
        for r in range(len(s)):
            ch = s[r]
            m[ch] += 1
            curLen = r - l + 1
            if curLen - max(m.values()) <= k:
                maxLen = max(maxLen, curLen)
            else:
                l_ch = s[l]
                m[l_ch] -= 1
                l += 1
        return maxLen


def main():
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))
    print(sol.characterReplacement("AABABBA", 1))


main()
