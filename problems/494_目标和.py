class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        # 问题转化：寻找nums的两个子集P和N，使得sum(P)-sum(N)=S
        # 又sum(P)+sum(N)=sum(nums) 可以求出sum(P)=sum(nums)+S // 2
        # 即在背包中寻找若干个数 使其和为sum(P)
        total = sum(nums)
        if total < S or (total + S) % 2 == 1:
            return 0
        target = (total + S) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        # 0-1背包问题 遍历每一个物品
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] += dp[j - num]
        return dp[target]
