# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 分治法 每次构建时传入的范围包括了全部所需的节点
        return self.build(0, len(postorder) - 1, 0, len(inorder) - 1, postorder, inorder)

    def build(self, post_left, post_right, in_left, in_right, postorder, inorder):
        if post_left > post_right or in_left > in_right:
            return None

        root = TreeNode(postorder[post_right])
        in_root = in_left
        while in_root <= in_right and inorder[in_root] != postorder[post_right]:
            in_root += 1
        left_len = in_root - in_left
        root.left = self.build(post_left, post_left + left_len - 1, in_left, in_root - 1, postorder, inorder)
        root.right = self.build(post_left + left_len, post_right - 1, in_root + 1, in_right, postorder, inorder)
        return root
