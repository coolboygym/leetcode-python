# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 先判断有无环 再找到入环点
        # 参考链接: https://leetcode-cn.com/problems/linked-list-cycle-ii/comments/307
        if head is None or head.next is None:
            return None
        p1 = head
        p2 = head
        flag = False
        while p2.next and p2.next.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                flag = True
                break

        if flag:
            q = head
            while q != p1:
                q = q.next
                p1 = p1.next
            return q
        return None
