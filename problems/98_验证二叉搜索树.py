# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys


class Solution(object):
    def __init__(self):
        self.last = sys.float_info.max * -1

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        if self.isValidBST(root.left):
            if self.last < root.val:
                self.last = root.val
                return self.isValidBST(root.right)
        return False
