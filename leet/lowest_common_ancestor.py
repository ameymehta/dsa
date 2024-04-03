# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.lca = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root, p, q)
        return self.lca

    def dfs(self, current_node, p, q):
        if not current_node:
            return False

        left = self.dfs(current_node.left, p, q)
        right = self.dfs(current_node.right, p, q)
        mid = (current_node == p) or (current_node == q)

        if (left + right + mid) > 1:
            self.lca = current_node

        return left or right or mid
