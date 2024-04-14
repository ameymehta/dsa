from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.isWord = False
        self.isAdded = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.children[ch]
        node.isWord = True

    def search(self, word):
        node = self.root
        for ch in word:
            node = node.childred.get(ch)
            if not node:
                return False
        return node.isWord


class Solution(object):

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        result = []
        trie = Trie()
        for word in words:
            trie.insert(word)

        node = trie.root
        for row in range(len(board)):
            for column in range(len(board[0])):
                self.dfs(board, node, row, column, "", result)

        return result

    def dfs(self, board, node, row, column, path, result):
        if node.isWord and not node.isAdded:
            result.append(path)
            node.isAdded = True
        if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]):
            return
        ch = board[row][column]
        node = node.children.get(ch)
        if not node:
            return
        board[row][column] = "#"
        path += ch
        self.dfs(board, node, row + 1, column, path, result)
        self.dfs(board, node, row - 1, column, path, result)
        self.dfs(board, node, row, column + 1, path, result)
        self.dfs(board, node, row, column - 1, path, result)
        board[row][column] = ch
