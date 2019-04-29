# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 链表问题 双指针
        if not head or k == 0:
            return head

        tail = head
        size = 1
        while tail.next:
            tail = tail.next
            size += 1

        # 如果k是链表大小的整数倍 则无需移动
        if k % size == 0:
            return head

        # 新的头节点是倒数第k个节点 即正数第 n-k+1 个节点
        i = size - (k % size) + 1
        dummy = ListNode(0)
        dummy.next = head
        prev, target = dummy, head
        for _ in range(i - 1):
            target = target.next
            prev = prev.next
        prev.next = None
        tail.next = head

        return target
