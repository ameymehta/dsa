# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.levels = []

    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.dfs(root)
        return self.levels
        
    def dfs(self, root):
        if root == None:
            return 0
        lh = self.dfs(root.left)
        rh = self.dfs(root.right)
        h = max(lh, rh) + 1
        if len(self.levels) < h:
            while len(self.levels) < h:
                self.levels.append([])
        self.levels[h-1].append(root.val)     
        return h