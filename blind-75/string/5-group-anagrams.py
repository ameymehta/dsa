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

    def group_anagrams_new(strs):
        result = []
        m = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            m[tuple(count)].append(s)
        return list(m.values())

    def main(self):
        self.group_anagrams_new(["eat", "tea", "tan", "ate", "nat", "bat"])