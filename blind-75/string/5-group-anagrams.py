from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        m = defaultdict(list)
        for s in strs:
            m[self.getSignature(s)].append(s)
        for k in m:
            result.append(m[k])
        return result
    
    def getSignature(self, s):
        result = []
        m = defaultdict(int)
        for ch in s:
            m[ch] += 1
        for k in m:
            result.append(k)
            result.append(str(m[k]))
        return ''.join(result)
