# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        l = dummy
        r = dummy
        for i in range(n + 1):
            r = r.next
        while r:
            r = r.next
            l = l.next
        l.next = l.next.next
        return dummy.next
