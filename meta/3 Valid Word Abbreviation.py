# 408. Valid Word Abbreviation
# https://leetcode.com/problems/valid-word-abbreviation/description/


class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        w = 0
        a = 0
        num = 0
        while w < len(word) and a < len(abbr):
            ch_w = word[w]
            ch_a = abbr[a]
            if ch_w == ch_a:
                w += 1
                a += 1
            elif ch_a.isnumeric():
                num = int(ch_a)
                a += 1
                while abbr[a].isnumeric():
                    num = (num * 10) + int(abbr[a])
                    a += 1
                w = w + num
            else:
                return False

        return w == len(word) and a == len(abbr)
