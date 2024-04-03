class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def paths_with_sum(root, sum):
  current, paths = [], []
  paths_with_sum_rec(root, sum, current, paths)
  return paths

def paths_with_sum_rec(root, sum, current, paths):
  if root == None:
    return False
  current.append(root.value)
  if root.value == sum and root.left == None and root.right == None:
    paths.append(list(current))
  else:
    paths_with_sum_rec(root.left, sum - root.value, current, paths)
    paths_with_sum_rec(root.right, sum - root.value, current, paths)
  del current[-1]

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  required_sum = 23
  print("Tree paths with required_sum " + str(required_sum) +
        ": " + str(paths_with_sum(root, required_sum)))

main()
