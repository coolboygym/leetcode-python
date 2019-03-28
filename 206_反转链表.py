# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        else:
            new_head = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return new_head


class Solution2(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:  # 边界条件
            return head
        cur = head  # 循环变量
        new_head = None  # 新的翻转单链表的表头
        while cur:
            tmp = cur.next
            cur.next = new_head
            new_head = cur  # 更新 新链表的表头
            cur = tmp
        return new_head
