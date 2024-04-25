# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.calc_height(root)

    def calc_height(self, root):
        if root == None:
            return 0

        left_height = self.calc_height(root.left)
        right_height = self.calc_height(root.right)

        return max(left_height, right_height) + 1
