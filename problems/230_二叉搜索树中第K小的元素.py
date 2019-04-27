# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        # 递归方法解决二叉树问题 其实就是在中序遍历的过程加了点额外的判断
        # 三步走：终止条件、返回值、访问当前节点时需要做的事情
        return self.find(root, 0, k)[2]

    def find(self, root, count, k):
        if root is None:
            return False, count, None

        res = self.find(root.left, count, k)
        if res[0]:
            return res

        # res[1]表示左子树的节点数量
        count = res[1] + 1
        if count == k:
            return True, count, root.val
        return self.find(root.right, count, k)


class Solution1:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        # yield from 是Python3.3之后的语法
        # 参考链接: https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst/comments/13786
        def gen(r):
            if r is not None:
                yield from gen(r.left)
                yield r.val
                yield from gen(r.right)

        it = gen(root)
        for _ in range(k):
            ans = next(it)
        return ans
