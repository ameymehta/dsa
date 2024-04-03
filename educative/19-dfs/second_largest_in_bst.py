class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def get_second_largest(root):
  if not root.right and root.left:
    return get_largest(root.left)
  if root.right and not root.right.left and not root.right.right:
    return root.value
  return get_second_largest(root.right)

def get_largest(root):
  if not root.right:
    return root.value
  return get_largest(root.right)


def main():
  root = TreeNode(5)
  root.left = TreeNode(2)
  root.right = TreeNode(12)
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(7)
  root.right.left.left = TreeNode(6)
  root.right.left.right = TreeNode(9)
  print get_second_largest(root)

main()
