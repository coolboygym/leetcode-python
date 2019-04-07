# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 递归三步走：判断终止条件 确定返回值 分析一次调用需要做哪些事
        return self.isBST(root)[0]

    def isBST(self, root):
        if root is None:
            return True, 0

        left = self.isBST(root.left)
        right = self.isBST(root.right)

        if left[0] and right[0]:
            return abs(right[1] - left[1]) <= 1, max(left[1], right[1]) + 1
        return False, 0
