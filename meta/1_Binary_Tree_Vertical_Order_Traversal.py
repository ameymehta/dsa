# 314. Binary Tree Vertical Order Traversal
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/
# Given the root of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be from left to right.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]

# Example 2:
# Input: root = [3,9,8,4,0,1,7]
# Output: [[4],[9],[3,0,1],[8],[7]]

# Example 3:
# Input: root = [3,9,8,4,0,1,7,null,null,null,2,5]
# Output: [[4],[9,5],[3,0,1],[8,2],[7]]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict
from collections import deque


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        nodes = defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, pos = queue.popleft()
            if not node:
                continue
            nodes[pos].append(node.val)
            queue.append((node.left, pos - 1))
            queue.append((node.right, pos + 1))
        result = []
        for key in sorted(nodes):
            result.append(nodes[key])
        return result
