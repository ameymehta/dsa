from collections import deque

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left, self.right = None, None

def traverse(root):
    q = deque()
    q.append(root)
    result = []
    while q:
        curLen = len(q)
        curLevel = []
        for i in range(curLen):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
            curLevel.append(cur.value)
        result.append(curLevel)
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
