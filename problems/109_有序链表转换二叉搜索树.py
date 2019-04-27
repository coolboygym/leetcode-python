# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution1(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        values = []
        while head is not None:
            values.append(head.val)
            head = head.next
        return self.build(values, 0, len(values) - 1)

    def build(self, values, begin, end):
        if begin > end:
            return None
        mid = begin + ((end - begin) >> 1)
        root = TreeNode(values[mid])
        root.left = self.build(values, begin, mid - 1)
        root.right = self.build(values, mid + 1, end)
        return root


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.build(head, None)

    def build(self, head, tail):
        if head == tail:
            return None
        # 通过快慢两个指针查找中点
        fast, slow = head, head
        while fast.next != tail and fast.next.next != tail:
            slow = slow.next
            fast = fast.next.next
        root = TreeNode(slow.val)
        # 边界条件可以通过实例来验证下
        root.left = self.build(head, slow)
        root.right = self.build(slow.next, tail)
        return root

