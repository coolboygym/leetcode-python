class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 摩尔投票法：https://blog.csdn.net/tinyjian/article/details/79110473
        # 维护两个候选者及其计数 一遍遍历并更新
        # 再一次遍历以确认候选者是否满足要求
        a, b, ca, cb, ans = None, None, 0, 0, []
        for num in nums:
            if num == a:
                ca += 1
            elif num == b:
                cb += 1
            elif ca == 0:
                a, ca = num, 1
            elif cb == 0:
                b, cb = num, 1
            else:
                ca, cb = ca - 1, cb - 1

        ca, cb = 0, 0
        for num in nums:
            if num == a:
                ca += 1
            elif num == b:
                cb += 1

        if ca > len(nums) // 3:
            ans.append(a)
        if cb > len(nums) // 3:
            ans.append(b)

        return ans
