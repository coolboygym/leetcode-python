# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        p1 = head
        p2 = head
        while p2.next and p2.next.next is not None:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False
