class Solution1(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 完全背包问题
        if amount == 0:
            return 0
        # 先排序是为了后面第二层循环可以提前终止
        coins.sort()
        # 当目标金额为0时 所需的硬币数也为0
        dp = [0]
        # 计算每一个目标金额下 最少的硬币组合
        # 两个for循环的不同顺序代表着两种不同的理解方式
        for i in range(1, amount + 1):
            dp.append(float('inf'))
            for coin in coins:
                if coin > i:
                    break
                # 状态转移方程：使用硬币j或不使用硬币j
                dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 完全背包问题
        if amount == 0:
            return 0
        dp = [0]
        # 无限/完全 背包问题 遍历每一个容量值
        # 计算每一个目标金额下 最少的硬币组合
        # 两个for循环的不同顺序代表着两种不同的理解方式
        for i in range(1, amount + 1):
            dp.append(float('inf'))
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == float('inf'):
            return -1
        return dp[amount]
