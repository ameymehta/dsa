class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

def getSecondLargest(root):
    # get largest node
    largest = root
    parent_of_largest = None
    while largest.right != None:
        parent_of_largest = largest
        largest = largest.right
    if largest.left:
        return largest.left
    else:
        return parent_of_largest
    

