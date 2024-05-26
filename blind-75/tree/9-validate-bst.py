# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        inf = sys.maxsize
        return self.helper(root, -inf, inf)

    def helper(self, node, low, high):
        if not node:
            return True
        if low < node.val < high:
            return self.helper(node.left, low, node.val) and self.helper(node.right, node.val, high)
        else:
            return False
