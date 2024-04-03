class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class TreeDiameter:
  def __init__(self):
    self.treeDiameter = 0

  def find_diameter(self, root):
    self.calc_height(root)
    return self.treeDiameter

  def calc_height(self, root):
    if root == None:
      return 0
  
    lh = self.calc_height(root.left)
    rh = self.calc_height(root.right)
    d = lh + rh + 1
    self.treeDiameter = max(self.treeDiameter, d)

    return max(lh, rh) + 1

def main():
  treeDiameter = TreeDiameter()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
  root.left.left = None
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  root.right.left.right.left = TreeNode(10)
  root.right.right.left.left = TreeNode(11)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))

main()
