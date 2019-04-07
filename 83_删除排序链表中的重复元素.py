# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        """
        递归套路解决链表问题：

        找终止条件：当head指向链表只剩一个元素的时候，自然是不可能重复的，因此直接return
        想想应该返回什么值：应该返回的自然是已经去重的链表的头节点
        每一步要做什么：宏观上考虑，此时head.next已经指向一个去重的链表了，
                     而根据第二步，我应该返回一个去重的链表的头节点。
                     因此这一步应该做的是判断当前的head和head.next是否相等，
                     如果相等则说明重了，返回head.next，否则返回head
        """
        if head is None or head.next is None:
            return head
        head.next = self.deleteDuplicates(head.next)
        return head.next if head.val == head.next.val else head
