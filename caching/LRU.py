class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache(object):

    def __init__(self, capacity):
        self.size = capacity
        self.map = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        # delete node
        node.prev.next = node.next
        node.next.prev = node.prev
        # add node
        temp = self.head.next
        self.head.next = node
        node.next = temp
        temp.prev = node
        node.prev = self.head
        return node.value
        

    def put(self, key, value):
        if key in self.map:
            node = self.map[key]
            node.value = value
            # delete node
            node.prev.next = node.next
            node.next.prev = node.prev
            # add node
            temp = self.head.next
            self.head.next = node
            node.next = temp
            temp.prev = node
            node.prev = self.head
        else:
            if len(self.map) == self.size:
                del self.map[self.tail.prev.key]
                # delete node
                self.tail.prev = self.tail.prev.prev
                self.tail.prev.next = self.tail
            node = Node(key, value)
            self.map[key] = node
            # add node
            temp = self.head.next
            self.head.next = node
            node.next = temp
            temp.prev = node
            node.prev = self.head

# driver code
def main():
    actions = ["LRUCache","put","put","get","put","get","put","get","get","get"]
    inputs = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]

    lru = LRUCache(2)
    for i in range(1, len(actions)):
        if actions[i] == "put":
            lru.put(inputs[i][0], inputs[i][1])
            print(str(i) + ". put")
        elif actions[i] == "get":
            value = lru.get(inputs[i][0])
            print(str(i) + ". " + str(value))

main()
