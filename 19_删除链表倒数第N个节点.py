# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # 双指针 当一个指针到达末尾时 另一个指向待删除节点的父节点
        if head is None or head.next is None:
            return None

        right = head
        for _ in range(n):
            right = right.next

        if right is None:
            return head.next

        left = head
        right = right.next
        while right is not None:
            right = right.next
            left = left.next
        target = left.next
        left.next = target.next
        target.next = None
        return head
