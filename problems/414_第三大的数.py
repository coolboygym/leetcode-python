class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 按序做比较 忽略重复值
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num == max1 or num == max2 or num == max3:
                continue
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
        return max1 if max3 == float('-inf') else max3
