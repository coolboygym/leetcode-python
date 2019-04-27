class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 直接将dp数组定义为和为i时组合的个数
        # 初始化起始元素，若元素=目标值，则组合结果就是1
        dp = [1]
        # 无限/完全 背包问题 遍历每一个容量值
        for i in range(1, target + 1):
            dp.append(0)
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]

        return dp[target]
