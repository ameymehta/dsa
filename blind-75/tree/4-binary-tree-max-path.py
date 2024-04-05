# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.maxSum = 0

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        pathSum = 0
        self.dfs(root, pathSum)
        return self.maxSum

    def dfs(self, root, pathSum):
        if root == None:
            return 0
        leftPathSum = self.dfs(root.left, pathSum)
        rightPathSum = self.dfs(root.right, pathSum)
        self.maxSum = max(self.maxSum, leftPathSum + rightPathSum + root.val)
        pathSum += root.val
        return pathSum