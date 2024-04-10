# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:
            return ""
        result = []
        q = deque()
        q.append(root)
        while q:
            curNode = q.popleft()
            if curNode:
                result.append(str(curNode.val))
                q.append(curNode.left)
                q.append(curNode.right)
            else:
                result.append("")
        return ",".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        arr = data.split(",")
        root = TreeNode(arr[0])
        q = deque()
        q.append(root)
        i = 1
        while q:
            curNode = q.popleft()
            if i < len(arr) and arr[i]:
                curNode.left = TreeNode(int(arr[i]))
                q.append(curNode.left)
            i += 1
            if i < len(arr) and arr[i]:
                curNode.right = TreeNode(int(arr[i]))
                q.append(curNode.right)
            i += 1
        return root
