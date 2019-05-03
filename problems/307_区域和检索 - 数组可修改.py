"""
segment tree
参考：https://leetcode.com/articles/a-recursive-approach-to-segment-trees-range-sum-queries-lazy-propagation/
"""


class SegmentTree(object):

    def __init__(self, nums):
        self.tree = [0] * len(nums) * 4
        self.nums = nums
        self.build(0, 0, len(self.nums) - 1)

    def build(self, idx, lo, hi):
        if hi < lo:
            return
        if lo == hi:
            self.tree[idx] = self.nums[lo]
            return
        m = (lo + hi) / 2
        self.build(idx * 2 + 1, lo, m)
        self.build(idx * 2 + 2, m + 1, hi)
        self.tree[idx] = self.tree[idx * 2 + 1] + self.tree[idx * 2 + 2]

    def query(self, idx, lo, hi, i, j):
        if i < lo or j > hi:
            return 0
        if i <= lo and j >= hi:
            return self.tree[idx]
        m = (lo + hi) / 2
        if i > m:
            return self.query(idx * 2 + 2, m + 1, hi, i, j)
        if j <= m:
            return self.query(idx * 2 + 1, lo, m, i, j)
        return self.query(idx * 2 + 2, m + 1, hi, m + 1, j) + self.query(idx * 2 + 1, lo, m, i, m)

    def update(self, idx, lo, hi, array_idx, value):
        self.nums[array_idx] = value
        if lo == hi:
            self.tree[idx] = value
            return
        m = (lo + hi) / 2
        if array_idx > m:
            self.update(idx * 2 + 2, m + 1, hi, array_idx, value)
        elif array_idx <= m:
            self.update(idx * 2 + 1, lo, m, array_idx, value)
        self.tree[idx] = self.tree[idx * 2 + 1] + self.tree[idx * 2 + 2]


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.seg = SegmentTree(nums)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.seg.update(0, 0, len(self.seg.nums) - 1, i, val)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.seg.query(0, 0, len(self.seg.nums) - 1, i, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
