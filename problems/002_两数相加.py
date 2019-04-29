# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 同时遍历两个链表 每次往结果中加一位 最后如果还有进位则保留
        dummy = ListNode(0)
        curr_res = dummy
        carry = 0
        while l1 or l2:
            x1 = l1.val if l1 else 0
            x2 = l2.val if l2 else 0
            s = carry + x1 + x2
            carry = s // 10
            curr_res.next = ListNode(s % 10)
            curr_res = curr_res.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry > 0:
            curr_res.next = ListNode(carry)
        return dummy.next
