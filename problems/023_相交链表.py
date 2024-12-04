# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution0(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        tailA = headA
        tailB = headB
        sizeA = 1
        sizeB = 1
        while tailA.next:
            tailA = tailA.next
            sizeA += 1
        while tailB.next:
            tailB = tailB.next
            sizeB += 1
        if tailA != tailB:  # 如果相交 尾节点一定相同
            return None
        currA = headA
        currB = headB
        sizeDiff = sizeA - sizeB
        if sizeDiff > 0:    # A链更长 移动指针进行对齐
            temp = sizeDiff
            while temp > 0:
                currA = currA.next
                temp -= 1
        else:               # B链更长
            temp = sizeB - sizeA
            while temp > 0:
                currB = currB.next
                temp -= 1
        while currA:        # 同时移动 找到交点
            if currA == currB:
                return currA
            currA = currA.next
            currB = currB.next
        return None
    

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        # 两个指针都遍历A+B链表 最终会在交点相遇 或者同时为None
        if not headA or not headB:
            return None
        currA = headA
        currB = headB
        while(currA != currB):
            currA = currA.next if currA is not None else headB
            currB = currB.next if currB is not None else headA
        return currA