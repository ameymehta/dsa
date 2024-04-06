from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root == None:
            return result
        q = deque()
        q.append(root)
        while  q:
            current_level = []
            current_len = len(q)
            for i in range(current_len):
                current_node = q.popleft()
                current_level.append(current_node.val)
                if current_node.left:
                    q.append(current_node.left)
                if current_node.right:
                    q.append(current_node.right)
            result.append(current_level)
        return result