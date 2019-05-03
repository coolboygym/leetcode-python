# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 单调队列
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        d = {}
        length = 0
        stack = []
        while head:
            while stack and stack[-1][-1] < head.val:
                idx, val = stack.pop(-1)
                d[idx] = head.val
            stack.append((length, head.val))
            length += 1
            head = head.next

        result = [0] * length
        for k, v in d.items():
            result[k] = v
        return result
