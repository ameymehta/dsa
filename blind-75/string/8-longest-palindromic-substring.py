class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        final = ""
        for i in range(len(s)):
            # check palindrome for odd cases abcba
            substr = self.helper(s, i, i)
            if len(substr) > len(final):
                final = substr
            # check palindrome for even cases abccba
            substr = self.helper(s, i, i + 1)
            if len(substr) > len(final):
                final = substr
        return final

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # return the palindromic sub-string
        return s[l + 1 : r]
