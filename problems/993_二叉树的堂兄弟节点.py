# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# level-order traversal
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        l = [root]
        l2 = []
        while l:
            node = l.pop(0)
            if node:
                l2.append(node.left)
                l2.append(node.right)
            if not l:
                l3 = [node.val if node else None for node in l2]
                if x in l3 and y in l3:
                    x_idx = l3.index(x)
                    y_idx = l3.index(y)
                    small = min(x_idx, y_idx)
                    large = max(x_idx, y_idx)
                    if large == small + 1 and small % 2 == 0:
                        return False
                    else:
                        return True
                l = l2
                l2 = []
        return False
