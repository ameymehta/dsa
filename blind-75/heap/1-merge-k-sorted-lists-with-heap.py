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
    
    # added count as tie breaker when heapq implementation compares node.val and if there is a tie
    def mergeKLists__2026(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        h = []
        count = 0
        for node in lists:
            if node:
                heapq.heappush(h, (node.val, count, node))
                count += 1
        dummy = ListNode()
        cur = dummy
        while h:
            val, cnt, node = heapq.heappop(h)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(h, (node.next.val, count, node.next))
                count += 1
        return dummy.next
