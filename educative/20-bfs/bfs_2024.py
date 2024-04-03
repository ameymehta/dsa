from collections import deque

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None

def traverse(root):
    result = []
    if root == None:
        return result
    q = deque()
    q.append(root)
    while q:
        cur_len = len(q)
        cur_level = []
        for i in range(cur_len):
            cur_node = q.popleft()
            cur_level.append(cur_node.value)
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        result.append(cur_level)
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level order traversal: " + str(traverse(root)))


main()
