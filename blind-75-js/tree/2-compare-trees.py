# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        return self.dfs(p, q)

    def dfs(self, p, q):
        left_tree_same = False
        right_tree_same = False
        value_same = p.val == q.val
        if p.left == None and q.left == None:
            left_tree_same = True
        elif p.left and q.left:
            left_tree_same = self.dfs(p.right, q.right)
        if p.right == None and q.right == None:
            right_tree_same = True
        elif p.right and q.right:
            right_tree_same = self.dfs(p.right, q.right)
        return value_same and left_tree_same and right_tree_same
