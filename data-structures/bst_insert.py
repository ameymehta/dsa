class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(str(root.info) + " ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

# Node is defined as
# self.left (the left child of the node)
# self.right (the right child of the node)
# self.info (the value of the node)

    def insert(self, val):
        # Enter you code here.
        if self.root is None:
            self.root = Node(val)
        else:
            self.insert_rec(self.root, val)

    def insert_rec(self, root, val):
        if val <= root.info:
            if root.left is None:
                root.left = Node(val)
            else:
                self.insert_rec(root.left, val)
        elif val > root.info:
            if root.right is None:
                root.right = Node(val)
            else:
                self.insert_rec(root.right, val)


def main():
    tree = BinarySearchTree()
    arr = [4, 2, 3, 1, 7, 6]
    for i in range(6):
        tree.insert(arr[i])
    preOrder(tree.root)


main()
