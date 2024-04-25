class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        for r in range(len(board)):
            for c in range(len(board[0])):
                if self.dfs(board, word, r, c, 0):
                    return True

        return False

    def dfs(self, board, word, r, c, match):
        if match == len(word):
            return True
        if (
            r < 0
            or r >= len(board)
            or c < 0
            or c >= len(board[0])
            or board[r][c] != word[match]
        ):
            return False

        ch = board[r][c]
        board[r][c] = "#"

        right = self.dfs(board, word, r + 1, c, match + 1)
        left = self.dfs(board, word, r - 1, c, match + 1)
        top = self.dfs(board, word, r, c - 1, match + 1)
        bottom = self.dfs(board, word, r, c + 1, match + 1)

        if right or left or top or bottom:
            return True

        board[r][c] = ch
        return False
