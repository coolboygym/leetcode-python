# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 两个堆栈实现 一次循环中遍历两个栈 代码工整而优美
        if root is None:
            return []

        res = []
        s1 = collections.deque()
        s2 = collections.deque()
        s1.append(root)
        while len(s1) > 0 or len(s2) > 0:
            temp_res = []
            while len(s1) > 0:
                curr_node = s1.pop()
                temp_res.append(curr_node.val)
                if curr_node.left is not None:
                    s2.append(curr_node.left)
                if curr_node.right is not None:
                    s2.append(curr_node.right)
            if temp_res:
                res.append(temp_res)
            temp_res = []
            while len(s2) > 0:
                curr_node = s2.pop()
                temp_res.append(curr_node.val)
                if curr_node.right is not None:
                    s1.append(curr_node.right)
                if curr_node.left is not None:
                    s1.append(curr_node.left)
            if temp_res:
                res.append(temp_res)

        return res
