class WordDictionary(object):

    def __init__(self):
        self.trie = {}

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        t = self.trie
        for ch in word:
            if ch not in t:
                t[ch] = {}
            t = t[ch]
        t["-"] = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        t = self.trie
        return self.searchInTrie(word, t)

    def searchInTrie(self, word, t):
        for i, ch in enumerate(word):
            if ch == ".":
                for key in t:
                    return self.searchInTrie(word[i + 1 :], t[key])
            if ch not in t:
                return False
            t = t[ch]
        return "-" in t


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
