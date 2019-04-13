class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 问题转化：在n个数中选出若干个使其和恰为n个数总和的一半
        n = len(nums)
        if n <= 1:
            return False

        total = sum(nums)
        # 如果总和是奇数 肯定无法分成相同的两个子集
        if total % 2 == 1:
            return False

        target = total // 2
        dp = []
        # 一维滚动数组 由于只要判断是否 因此初始化为True/False
        for i in range(target + 1):
            dp.append(nums[0] == i)

        for num in nums[1:]:
            for j in range(target, num - 1, -1):
                # 状态转移方程：不使用第i个物品或者使用第i个物品
                dp[j] = (dp[j] or dp[j - num])

        return dp[target]
