class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self):

    def insert(root, data):
        if data <= root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                insert(root.left, data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                insert(root.right, data)

    def contains(root, data):
        if root.data == data:
            return True
        else if data <= root.data:
            if root.left is None:
                return False
            else:
                return contains(root.left, data)
        else:
            if root.right is None:
                return False
            else:
                return contains(root.right, data)

    def print_inorder(root):
        if root.left is not None:
            print_inorder(root.left)
        print(data)
        if root.right is not None:
            print_inorder(root.right)

    def print_preorder(root):
        print(data)
        if root.left is not None:
            print_preorder(root.left)
        if root.right is not None:
            print_preorder(root.right)

    def print_postorder(root):
        if root.left is not None:
            print_postorder(root.left)
        if root.right is not None:
            print_postorder(root.right)
        print(data)
