# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        l1 = head
        head2 = Node(0)
        l2 = head2
        random_map = {}
        random_map[None] = None
        index = 0
        while l1:
            new_node = Node(l1.val)
            l2.next = new_node
            l2 = l2.next
            l1 = l1.next
            random_map[index] = new_node
            index += 1

        l1 = head
        l2 = head2.next
        while l1:
            l2.random = random_map[l1.random]
            l1 = l1.next
            l2 = l2.next

        return head2.next
