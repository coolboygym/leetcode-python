# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 朴素解法 重建整棵树
        nodes = []
        values = []
        self.inorder(root, nodes, values)
        values.sort()
        for i in range(len(nodes)):
            nodes[i].val = values[i]
        return root

    def inorder(self, root, nodes, values):
        if root is None:
            return
        self.inorder(root.left, nodes, values)
        nodes.append(root)
        values.append(root.val)
        self.inorder(root.right, nodes, values)


class Solution1(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 借助Morris中序遍历
        # 参考链接: https://leetcode-cn.com/problems/recover-binary-search-tree/comments/66315
        n1, n2 = None, None
        curr1, prev = root, None
        while curr1:
            curr2 = curr1.left
            if curr2:
                while curr2.right and curr2.right is not curr1:
                    curr2 = curr2.right
                if not curr2.right:
                    curr2.right = curr1
                    curr1 = curr1.left
                    continue
                else:
                    curr2.right = None

            if prev and prev.val > curr1.val:
                if not n1:
                    n1, n2 = prev, curr1
                else:
                    n2 = curr1
            prev = curr1
            curr1 = curr1.right
        n1.val, n2.val = n2.val, n1.val
