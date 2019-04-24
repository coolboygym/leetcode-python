# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 类比环形链表II 使用双指针 巧妙结合给定链表的结构
        p, q = headA, headB
        while p and q:
            p = p.next
            q = q.next
        if p is None:
            return self.help(headA, headB, q)
        else:
            return self.help(headB, headA, p)

    def help(self, headA, headB, node):
        p, q = headA, headB
        while node:
            node = node.next
            q = q.next
        while p:
            if p is q:
                return p
            p = p.next
            q = q.next
        return None


class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        """
        很优雅的解法 参考https://leetcode-cn.com/problems/intersection-of-two-linked-lists/submissions/
        定义两个指针, 第一轮让两个到达末尾的节点指向另一个链表的头部, 最后如果相遇则为交点(在第一轮移动中恰好抹除了长度差)
        两个指针等于移动了相同的距离, 有交点就返回, 无交点就是各走了两条指针的长度后同时为None 退出循环并返回None
        """

        if headA is None or headB is None:
            return None
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa
