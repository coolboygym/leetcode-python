# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 分治法 递归构建左右子树
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, left, right):
        if left > right:
            return None
        mid = left + ((right - left) >> 1)
        root = TreeNode(nums[mid])
        root.left = self.build(nums, left, mid - 1)
        root.right = self.build(nums, mid + 1, right)
        return root
