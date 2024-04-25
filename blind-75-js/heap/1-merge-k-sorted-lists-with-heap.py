import heapq


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        for node in lists:
            if node:
                heapq.heappush(h, (node.val, node))
        dummy = ListNode(0)
        cur = dummy
        while h:
            node = heapq.heappop(h)[1]
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(h, (node.next.val, node.next))
        return dummy.next
