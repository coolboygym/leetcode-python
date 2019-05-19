# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def check(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 and node2:
                return False
            if not node2 and node1:
                return False
            if node1.val != node2.val:
                return False
            return check(node1.left, node2.left) and check(node1.right, node2.right) \
                   or check(node1.left, node2.right) and check(node1.right, node2.left)

        return check(root1, root2)