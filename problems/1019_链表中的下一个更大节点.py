# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        # 单调队列
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


class Solution1(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        # 先求链表长度 再用单调队列
        l = 0
        curr = head
        while curr:
            l += 1
            curr = curr.next

        q = []
        ans = [0] * l
        curr = head
        i = 0
        while curr:
            while q and q[-1][0] < curr.val:
                ans[q[-1][1]] = curr.val
                q.pop()
            q.append((curr.val, i))
            i += 1
            curr = curr.next
        return ans
