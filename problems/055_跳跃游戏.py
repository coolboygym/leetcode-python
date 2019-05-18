class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        参考：https://leetcode-cn.com/problems/jump-game/comments/6694
        从后往前遍历数组，如果遇到的元素可以到达最后一行，则截断后边的元素。
        否则继续往前，弱最后剩下的元素大于1个，则可以判断为假。
        否则就是真，时间复杂度O(n)就可以
        """
        # 这里的n可以理解为当前位置和下一个最近的着陆点之间的距离
        n = 1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] >= n:
                n = 1
            else:
                n += 1
            if i == 0 and n > 1:
                return False
        return True
