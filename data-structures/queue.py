class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty():
        return (self.head is None)

    def peak():
        return self.head.data

    def add(data):
        new_node = Node(data)
        if tail is not None:
            tail.next = new_node
        tail = new_node
        if head is None:
            head = new_node

    def remove():
        data = head.data
        head = head.next
        return data
