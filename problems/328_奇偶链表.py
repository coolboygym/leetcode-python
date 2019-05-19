# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        odd = head
        even = head.next

        start1 = odd
        start2 = even

        while odd:
            if not odd.next or not odd.next.next:
                break
            odd.next = odd.next.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = start2
        return start1