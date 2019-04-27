# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 借助拓扑排序
        if root is None:
            return []

        res = []
        que = collections.deque()
        que.append((root, 0))
        while len(que) > 0:
            item = que.popleft()
            node, i = item[0], item[1]
            if node is not None:
                if len(res) <= i:
                    res.append([])
                res[i].append(node.val)
                que.append((node.left, i + 1))
                que.append((node.right, i + 1))

        return res


class Solution1(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # 借助前序遍历实现层次遍历
        res = []
        self.preOrder(root, 0, res)
        return res

    def preOrder(self, root, depth, result_array):
        if root is None:
            return
        if depth >= len(result_array):
            result_array.append([])
        result_array[depth].append(root.val)
        self.preOrder(root.left, depth + 1, result_array)
        self.preOrder(root.right, depth + 1, result_array)
