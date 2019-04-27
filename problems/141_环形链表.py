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
        # 快慢指针 如果有环 在慢指针到达尾部时 快指针一定会到达尾部两次 即一定会超过慢指针一次
        # 快指针每次比慢指针多走一步 则一定有一次会和慢指针相遇 类比生活中的追逐
        if head is None or head.next is None:
            return False
        p1 = head
        p2 = head
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False
