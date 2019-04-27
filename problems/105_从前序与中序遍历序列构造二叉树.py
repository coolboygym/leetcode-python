# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 分治法 每次构建时传入的范围包括了全部所需的节点
        return self.build(0, len(preorder) - 1, 0, len(inorder) - 1, preorder, inorder)

    def build(self, pre_left, pre_right, in_left, in_right, preorder, inorder):
        if pre_left > pre_right or in_left > in_right:
            return None

        root = TreeNode(preorder[pre_left])
        in_root = in_left
        while in_root <= in_right and inorder[in_root] != preorder[pre_left]:
            in_root += 1
        left_len = in_root - in_left
        root.left = self.build(pre_left + 1, pre_left + left_len, in_left, in_root - 1, preorder, inorder)
        root.right = self.build(pre_left + left_len + 1, pre_right, in_root + 1, in_right, preorder, inorder)
        return root
