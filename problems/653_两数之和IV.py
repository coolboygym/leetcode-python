# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        s = set()
        result = self.preOrderFind(s, root, k)
        return result

    def preOrderFind(self, values, root, k):
        if root is None:
            return False
        if (k - root.val) in values:
            return True
        values.add(root.val)
        return self.preOrderFind(values, root.left, k) or self.preOrderFind(values, root.right, k)

