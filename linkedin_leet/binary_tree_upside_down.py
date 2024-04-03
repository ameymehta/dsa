# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root and root.left:
            result = self.upsideDownBinaryTree(root.left)
            root.left.right = root
            if root.right:
                root.left.left = root.right
            root.left = None
            root.right = None
            return result
        else:
            return root