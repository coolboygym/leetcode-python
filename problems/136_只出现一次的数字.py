class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 借助异或操作的特点 两个相同的数异或结果为0
        result = nums[0]
        for i in range(1, len(nums)):
            result = nums[i] ^ result
        return result
