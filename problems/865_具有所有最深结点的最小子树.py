# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        """
        根据题意描述, 是要找到一个节点, 以该节点为根的树中包含所有最大深度节点
        那么只要左子树的最大深度等于右子树的最大深度, 就说明左右子树都包含最大
        深度节点, 此时该节点就是满足条件的节点. 否则进入深度较大的那侧继续判断
        """
        if root is None:
            return root
        left = self.depth(root.left)
        right = self.depth(root.right)
        if left == right:
            return root
        if left < right:
            return self.subtreeWithAllDeepest(root.right)
        else:
            return self.subtreeWithAllDeepest(root.left)

    def depth(self, root):
        if root is None:
            return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
