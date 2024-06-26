# A message containing letters from A-Z can be encoded into numbers using the following mapping:
# 'A' -> "1"
# 'B' -> "2"
# 'Z' -> "26"
# To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above
# (there may be multiple ways).
# For example, "11106" can be mapped into:
# "AAJF" with the grouping (1 1 10 6)
# "KJF" with the grouping (11 10 6)

# Example 1:
# Input: s = "12"
# Output: 2
# Explanation: "12" could be decoded as "AB" (1 2) or "L" (12).

# Example 2:
# Input: s = "226"
# Output: 3
# Explanation: "226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

# Example 3:
# Input: s = "06"
# Output: 0
# Explanation: "06" cannot be mapped to "F" because of the leading zero ("6" is different from "06").


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo = {}

        def decode_helper(index):
            if index == len(s):
                return 1
            if s[index] == "0":
                return 0
            if index in memo:
                return memo[index]

            ways = decode_helper(index + 1)
            if index + 1 < len(s) and int(s[index : index + 2]) <= 26:
                ways += decode_helper(index + 2)

            memo[index] = ways
            return ways

        return decode_helper(0)
