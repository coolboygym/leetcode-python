# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        """
        1. 快慢指针找到终点 注意要保证当节点数为奇数时前半部分更长
        2. 拆成两个链表 并反转后一个链表
        3. 遍历两个链表 把后一个链表的节点塞到前一个链表中
        """
        if head is None or head.next is None:
            return head
        slow, fast = head, head

        # 这里的判断条件保证前半部分不会更短
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        back = slow.next
        slow.next = None
        back = self.reverseList(back)
        front = head
        while front and back:
            t1, t2 = front.next, back.next
            front.next = back
            back.next = t1
            front, back = t1, t2

    def reverseList(self, head):
        cur = head
        new_head = None
        while cur:
            tmp = cur.next
            cur.next = new_head
            new_head = cur
            cur = tmp
        return new_head
