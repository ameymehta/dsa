class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

def findLeaves(root):
    result = []
    def dfs(root):
        if not root:
            return 0
        depth = max(dfs(root.left),dfs(root.right))+1
        if len(result)<depth:
            result.append([])
        result[depth-1].append(root.value)
        return depth
    dfs(root)
    return result

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print(str(findLeaves(root)))

main()
