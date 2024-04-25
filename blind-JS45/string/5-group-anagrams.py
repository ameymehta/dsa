from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        groups = defaultdict(list)

        for s in strs:
            groups[self.getSignature(s)].append(s)

        for k in groups:
            result.append(groups[k])

        return result

    def getSignature(self, s):
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        result = []
        for k in freq:
            result.append(k)
            result.append(str(freq[k]))
        return "".join(result)
