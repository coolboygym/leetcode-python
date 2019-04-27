# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 中序遍历的迭代实现 通过条件判断的顺序来标识根节点的入栈次数 很巧妙
        # 参考链接: https://leetcode-cn.com/problems/binary-tree-inorder-traversal/comments/2706
        res = []
        stack = []
        cur = root
        while cur or len(stack) > 0:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
