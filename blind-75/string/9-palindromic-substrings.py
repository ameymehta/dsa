class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = 0
        for i in range(len(s)):
            # check palindrome for odd cases abcba
            subtotal = self.helper(s, i, i)
            total += subtotal
            # check palindrome for even cases abccba
            subtotal = self.helper(s, i, i + 1)
            total += subtotal
        return total

    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # num of possible palindromes from this check will be length mod 2
        return (r - l) // 2
