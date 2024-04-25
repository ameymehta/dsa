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
        char_freq = {}
        left = 0
        max_len = 0
        for right in range(len(s)):
            right_ch = s[right]
            if right_ch not in char_freq:
                char_freq[right_ch] = 0
            char_freq[right_ch] += 1

            cur_len = right - left + 1
            if cur_len - max(char_freq.values()) <= k:
                max_len = max(max_len, cur_len)
            else:
                left_ch = s[left]
                char_freq[left_ch] -= 1
                if char_freq[left_ch] == 0:
                    del char_freq[left_ch]
                left += 1
        return max_len


def main():
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))
    print(sol.characterReplacement("AABABBA", 1))


main()
