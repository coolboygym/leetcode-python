# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution1(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # BFS实现层次遍历
        if root is None:
            return 0

        curr_set = {root}
        level = 0
        while len(curr_set) > 0:
            next_set = set()
            for node in curr_set:
                # 是否要将访问子节点是独立的两个问题 直接两个判断即可
                if node.left is not None:
                    next_set.add(node.left)
                if node.right is not None:
                    next_set.add(node.right)
            level += 1
            curr_set = next_set
        return level


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return 0 if root is None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
