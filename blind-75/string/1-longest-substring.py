class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        freq = {}
        max_len  = 0
        for end in range(len(s) - 1):
            current = s[end]
            if current not in freq:
                freq[current] = end
                max_len = max(max_len, end - start + 1)
            else:
                start = freq[current] + 1
                freq[current] = end
                max_len = max(max_len, end - start + 1)
        return max_len
    
def main():
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))
    print(sol.lengthOfLongestSubstring("bbbbb"))
    print(sol.lengthOfLongestSubstring("pwwkew"))

main()
