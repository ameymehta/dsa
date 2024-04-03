class WordDistance(object):

    def __init__(self, wordsDict):
        """
        :type wordsDict: List[str]
        """
        self.dict = {}
        self.len = len(wordsDict)
        for i, w in enumerate(wordsDict):
            self.dict[w] = self.dict.get(w, []) + [i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        list1 = self.dict[word1]
        list2 = self.dict[word2]
        i, j = 0, 0
        minDist = self.len
        while i<len(list1) and j<len(list2):
            minDist = min(minDist, abs(list1[i] - list2[j]))
            if list1[i] <= list2[j]:
                i += 1
            else:
                j += 1
        return minDist
                
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)