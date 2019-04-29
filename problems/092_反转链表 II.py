# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if head is None or head.next is None or m >= n:
            return head

        dummy = ListNode(0)
        dummy.next = head
        h1 = head
        i = 1
        while i < m:
            i += 1
            h1 = h1.next

        p1 = h1.next
        p2 = p1.next
        p3 = p2.next
        while i < n:
            i += 1
            p2.next = p1
            p1 = p2
            p2 = p3
            if p3 is not None:
                p3 = p3.next
        h1.next.next = p2
        h1.next = p1

        return dummy.next
