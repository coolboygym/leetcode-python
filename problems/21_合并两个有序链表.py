# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 双指针 三while
        if l1 is None and l2 is None:
            return None

        dummy = ListNode(-1)
        curr = dummy
        while l1 is not None and l2 is not None:
            while l1 is not None and l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            if l1 is None:
                break
            while l2 is not None and l2.val <= l1.val:
                curr.next = l2
                l2 = l2.next
                curr = curr.next

        if l1 is not None:
            curr.next = l1
        elif l2 is not None:
            curr.next = l2
        else:
            curr.next = None

        return dummy.next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return None

        dummy = ListNode(-1)
        curr = dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
                curr = curr.next
            else:
                curr.next = l2
                l2 = l2.next
                curr = curr.next

        if l1 is not None:
            curr.next = l1
        elif l2 is not None:
            curr.next = l2
        else:
            curr.next = None

        return dummy.next
