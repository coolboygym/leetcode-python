# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 借助最小堆 实现K路归并排序
        from heapq import heappush, heappop

        if not lists:
            return None

        h = []
        for node in lists:
            if node is not None:
                heappush(h, (node.val, node))
        head = ListNode(-1)
        curr = head
        while h:
            node_tuple = heappop(h)
            curr.next = node_tuple[1]
            curr = curr.next
            if curr.next is not None:
                heappush(h, (curr.next.val, curr.next))

        return head.next
