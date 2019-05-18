class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 从第一个数开始count=1，遇到相同的就加1，遇到不同的就减1，减到0就重新换个数开始计数，总能找到出现最多的那个
        cnt, ret = 0, 0
        for num in nums:
            if cnt == 0:
                ret = num
            if num != ret:
                cnt -= 1
            else:
                cnt += 1
        return ret
