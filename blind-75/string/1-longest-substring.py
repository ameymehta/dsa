class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        index_map = {}
        max_len = 0
        for end in range(len(s) - 1):
            char = s[end]
            if char not in index_map:
                index_map[char] = end
                max_len = max(max_len, end - start + 1)
            else:
                start = index_map[char] + 1
                index_map[char] = end
                max_len = max(max_len, end - start + 1)
        return max_len


def main():
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbb"))
    print(sol.lengthOfLongestSubstring("pwwkew"))


main()
