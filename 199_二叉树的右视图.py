# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution1(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 借助前序遍历实现层次遍历 取每一层最右边的节点即为右视图
        res = []
        self.preOrder(root, 0, res)
        return [x[-1] for x in res]

    def preOrder(self, root, depth, result_array):
        if root is None:
            return
        if depth >= len(result_array):
            result_array.append([])
        result_array[depth].append(root.val)
        self.preOrder(root.left, depth + 1, result_array)
        self.preOrder(root.right, depth + 1, result_array)


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # BFS实现层次遍历 每层最右边节点输出
        if root is None:
            return []

        curr_nodes = [root]
        res = []
        while len(curr_nodes) > 0:
            next_set = []
            for node in curr_nodes:
                # 是否要将访问子节点是独立的两个问题 直接两个判断即可
                if node.left is not None:
                    next_set.append(node.left)
                if node.right is not None:
                    next_set.append(node.right)
            res.append(curr_nodes[-1].val)
            curr_nodes = next_set
        return res
