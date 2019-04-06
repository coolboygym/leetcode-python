import sys


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 贪心算法 记录最小值和次小值 通过IF条件保证序列的有序性
        a = sys.float_info.max
        b = sys.float_info.max
        for num in nums:
            if num <= a:
                a = num
            elif num <= b:
                b = num
            else:
                return True
        return False

