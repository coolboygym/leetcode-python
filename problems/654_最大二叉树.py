# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.build(nums, 0, len(nums) - 1)

    def build(self, nums, left, right):
        if left > right:
            return None
        if left == right:
            return TreeNode(nums[left])

        max_num, idx = nums[left], left
        for i in range(left + 1, right + 1):
            if nums[i] > max_num:
                max_num = nums[i]
                idx = i
        root = TreeNode(max_num)
        root.left = self.build(nums, left, idx - 1)
        root.right = self.build(nums, idx + 1, right)
        return root
