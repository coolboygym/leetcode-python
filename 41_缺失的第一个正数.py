class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 根据题目特点 借用位图的思想 把数组中的正数x都放置到x-1的位置 再扫描一遍即可
        n = len(nums)
        for i in range(n):
            curr = nums[i]
            while 0 < curr <= n and nums[curr - 1] != curr:
                nums[curr - 1], nums[i] = nums[i], nums[curr - 1]
                curr = nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
