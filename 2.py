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
        result = ListNode(0)
        add_one = 0
        l1_temp = l1
        l2_temp = l2
        res_temp = result
        while l1_temp is not None and l2_temp is not None:
            temp = l1_temp.val + l2_temp.val + add_one
            res_temp.val = temp % 10
            add_one = temp // 10

            res_temp = res_temp.next = ListNode(0)
            l2_temp = l2_temp.next
            l1_temp = l1_temp.next

        return result
