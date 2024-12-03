# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# 最直观做法 把链表的值放到数组 数组排序 然后再放回链表
class Solution0(object):
    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        values.sort()
        curr = head
        for i in range(len(values)):
            curr.val = values[i]
            curr = curr.next
        return head


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 针对链表的归并排序 时间复杂度O(nlogn)
        if head is None or head.next is None:
            return head
        prev = head
        slow = head.next
        fast = head.next.next
        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next
        prev.next = None    # 在prev处断开链表
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        dummy = ListNode(0)
        p = dummy
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        if l1:
            p.next = l1
        else:
            p.next = l2
        return dummy.next
