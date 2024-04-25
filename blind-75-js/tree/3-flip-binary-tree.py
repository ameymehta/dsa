# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        q = deque()
        q.append(root)
        while q:
            current_len = len(q)
            for i in range(current_len):
                current_node = q.popleft()
                if current_node.left and current_node.right:
                    current_node.left, current_node.right = (
                        current_node.right,
                        current_node.left,
                    )
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
        return root
