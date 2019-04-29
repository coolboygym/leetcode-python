class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 解决本题的核心: 如果前面某一段和为负数则舍弃
        max_so_far, max_ending_here = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_ending_here = max(max_ending_here + nums[i], nums[i])
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far


class Solution1(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        curr_sum = 0
        for num in nums:
            if curr_sum > 0:
                curr_sum += num
            else:
                curr_sum = num
            res = max(res, curr_sum)
        return res
