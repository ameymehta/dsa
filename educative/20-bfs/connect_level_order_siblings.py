from collections import deque

class TreeNode:
  def __init__(self, value, right=None, left=None, next=None):
    self.value = value
    self.right = right
    self.left = left
    self.next = next

def connect_level_order_siblings(root):
  q = deque()
  q.append(root)
  while q:
    levelsize = len(q)
    prevNode = None
    for i in range(levelsize):
      node = q.popleft()
      if prevNode:
        prevNode.next = node
      prevNode = node
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

main()
