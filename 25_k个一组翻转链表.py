# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        check_node = head
        num = 0
        while num < k and check_node is not None:
            num += 1
            check_node = check_node.next
        if num == k:
            count = 0
            curr = head
            temp = None
            new_head = None
            while count < k:
                temp = curr.next
                curr.next = new_head
                new_head = curr
                curr = temp
                count += 1
            if temp is not None:
                head.next = self.reverseKGroup(temp, k)
            return new_head
        else:
            return head
