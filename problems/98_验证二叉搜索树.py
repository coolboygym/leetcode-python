# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def __init__(self):
        self.last = float('-inf')

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # BST的特点是中序遍历为升序 可以在中序遍历时中记录当前最大值 对于不符合要求的输入可以提前返回
        # 参考链接: https://leetcode-cn.com/problems/validate-binary-search-tree/comments/3165
        if root is None:
            return True
        if self.isValidBST(root.left):
            if self.last < root.val:
                self.last = root.val
                return self.isValidBST(root.right)
        return False
