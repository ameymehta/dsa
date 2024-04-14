# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        cur = head
        arr = []
        while cur:
            arr.append(cur)
            cur = cur.next
        l = 0
        r = len(arr) - 1
        last = head
        while l < r:
            arr[l].next = arr[r]
            l += 1
            if l == r:
                last = arr[r]
                break
            arr[r].next = arr[l]
            r -= 1
            last = arr[l]
        if last:
            last.next = None
