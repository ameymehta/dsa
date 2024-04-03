class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def root_to_leaf_sum(root):
  return root_to_leaf_sum_rec(root, 0)

def root_to_leaf_sum_rec(root, sum):
  if root == None:
    return 0

  sum = 10*sum + root.value

  if root.left == None and root.right == None:
    return sum

  return root_to_leaf_sum_rec(root.left, sum) + root_to_leaf_sum_rec(root.right, sum)
  

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(root_to_leaf_sum(root)))


main()
