class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 两遍遍历 从左至右乘一遍 从右到左再乘一遍
        # 直接使用output数组 只需要O(1)的额外空间
        n = len(nums)
        output = [1 for _ in range(n)]
        for i in range(1, n):
            output[i] = output[i-1] * nums[i-1]
        product = 1
        for j in range(n-2, -1, -1):
            product *= nums[j+1]
            output[j] *= product
        return output
