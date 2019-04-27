# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # BFS实现层次遍历
        if root is None:
            return 0

        curr_set = {root}
        level = 1
        while len(curr_set) > 0:
            next_set = set()
            for node in curr_set:
                if node.left is None and node.right is None:
                    return level
                # 是否要将访问子节点是独立的两个问题 直接两个判断即可
                if node.left is not None:
                    next_set.add(node.left)
                if node.right is not None:
                    next_set.add(node.right)
            level += 1
            curr_set = next_set
        return level


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            if root.left and root.right:
                return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
            elif root.left:
                return 1 + self.minDepth(root.left)
            elif root.right:
                return 1 + self.minDepth(root.right)
            else:
                return 1
        else:
            return 0
