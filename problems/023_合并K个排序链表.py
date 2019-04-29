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
        # 借助最小堆 实现K路归并排序 时间复杂度O(Nlogk) N为总节点数 k为链表数
        # 这段代码LeetCode上Python3运行会报错 Python提交可以通过 和解释器的具体版本有关
        from heapq import heappush, heappop

        if not lists:
            return None

        h = []
        for node in lists:
            if node is not None:
                heappush(h, (node.val, node))
        dummy = ListNode(-1)
        curr = dummy
        while h:
            node_tuple = heappop(h)
            curr.next = node_tuple[1]
            curr = curr.next
            if curr.next:
                heappush(h, (curr.next.val, curr.next))

        return dummy.next
