class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 贪心算法 记录最小值和次小值 通过IF条件保证序列的有序性
        # 参考链接: https://leetcode-cn.com/problems/increasing-triplet-subsequence/comments/58833
        a = float('inf')
        b = float('inf')
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False
