class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty():
        return (self.top is None)

    def peak():
        return self.top.data

    def push(data):
        new_node = Node(data)
        new_node.next = self.top
        top = new_node

    def pop():
        data = top.data
        top = top.next
        return data
