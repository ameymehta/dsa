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

        def helper(node, low, high):
            if not node:
                return True
            if low < node.val < high:
                return helper(node.left, low, node.val) and helper(
                    node.right, node.val, high
                )
            else:
                return False

        return helper(root, -inf, inf)
