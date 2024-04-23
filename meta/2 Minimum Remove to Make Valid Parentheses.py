# 1249. Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
# Given a string s of '(' , ')' and lowercase English characters.
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Example 1:
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

# Example 2:
# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Example 3:
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.


class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        left_count = 0
        right_count = 0
        stack = []
        reverse_stack = []

        # first pass adds all chars but not extra rights
        for ch in s:
            if ch == "(":
                left_count += 1
            elif ch == ")":
                right_count += 1
            if right_count > left_count:
                right_count -= 1
            else:
                stack.append(ch)

        # second pass adds all chars but not extra lefts
        while stack:
            ch = stack.pop()
            if left_count > right_count and ch == "(":
                left_count -= 1
            else:
                reverse_stack.append(ch)

        # form string and return
        result = ""
        while reverse_stack:
            ch = reverse_stack.pop()
            result += ch

        return result
