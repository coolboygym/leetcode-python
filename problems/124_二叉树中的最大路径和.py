# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 递归三步走
        res = self.help(root)
        return max(res[0], res[1])

    def help(self, root):
        if root is None:
            return float('-inf'), float('-inf')
        left_res = self.help(root.left)
        right_res = self.help(root.right)
        max_path_with_root = max(root.val, root.val + left_res[0], root.val + right_res[0])
        max_path_without_root = max(left_res[0] + right_res[0] + root.val, left_res[0], right_res[0],
                                    left_res[1], right_res[1])
        return max_path_with_root, max_path_without_root


class Solution1(object):
    def __init__(self):
        # 借助一个全局变量及时保存当前的最大路径值
        self.result = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.help(root)
        return self.result

    def help(self, root):
        if root is None:
            return 0
        left = max(0, self.help(root.left))
        right = max(0, self.help(root.right))
        self.result = max(self.result, root.val + left + right)
        return max(left, right) + root.val

