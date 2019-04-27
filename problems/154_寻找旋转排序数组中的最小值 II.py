class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 二分搜索 解法比较巧妙 边界条件需要找实例来推导下：当数组中只有一个元素时怎么处理
        l, r = 0, len(nums) - 1
        while l < r:
            while l < r and nums[r] == nums[r - 1]:
                r -= 1
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]
