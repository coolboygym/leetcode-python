# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution1(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 拓扑排序
        if root is None:
            return []

        res = []
        que = collections.deque()
        que.append((root, 0))
        while len(que) > 0:
            item = que.popleft()
            node, i = item[0], item[1]
            if node:
                if len(res) <= i:
                    res.append([])
                res[i].append(node.val)
                que.append((node.left, i + 1))
                que.append((node.right, i + 1))

        return list(reversed(res))
