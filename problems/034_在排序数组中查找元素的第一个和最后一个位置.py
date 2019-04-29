class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 二分查找的扩展
        l = 0
        n = len(nums)
        r = n - 1

        # 找到第一个值等于target的元素下标
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] >= target:
                r = m - 1
            else:
                l = m + 1

        if l != n and nums[l] == target:
            i = l + 1
            while i < n and nums[i] == target:
                i += 1
            return [l, i - 1]

        return [-1, -1]


class Solution1:
    def searchRange(self, nums, target):
        # 朴素解法 一次遍历
        loc = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                if loc[0] == -1:
                    loc[0] = i
                if loc[0] != -1:
                    loc[1] = i
        return loc


if __name__ == '__main__':
    s = Solution()
    assert s.searchRange([5, 7, 7, 8, 8, 10], 8) == [3, 4]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
    assert s.searchRange([5, 7, 7, 8, 8, 10], 5) == [0, 0]
