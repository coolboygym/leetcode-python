# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 两个堆栈实现 每次循环都同时遍历两个栈 代码工整而优美
        if root is None:
            return []

        res = []
        s1 = []
        s2 = []
        s1.append(root)
        while len(s1) > 0 or len(s2) > 0:
            temp_res = []
            while len(s1) > 0:
                curr_node = s1.pop()
                temp_res.append(curr_node.val)
                if curr_node.left:
                    s2.append(curr_node.left)
                if curr_node.right:
                    s2.append(curr_node.right)
            if temp_res:
                res.append(temp_res)
            temp_res = []
            while len(s2) > 0:
                curr_node = s2.pop()
                temp_res.append(curr_node.val)
                if curr_node.right:
                    s1.append(curr_node.right)
                if curr_node.left:
                    s1.append(curr_node.left)
            if temp_res:
                res.append(temp_res)

        return res
