class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        """
        参考链接: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/comments/10285
        当k大于等于数组长度一半时, 问题退化为贪心问题此时采用 买卖股票的最佳时机 II
        的贪心方法解决可以大幅提升时间性能, 对于其他的k, 可以采用 买卖股票的最佳时机 III
        的方法来解决, 在III中定义了两次买入和卖出时最大收益的变量, 在这里就是k租这样的
        变量, 即问题IV是对问题III的推广, t[i][0]和t[i][1]分别表示第i比交易买入和卖出时
        各自的最大收益
        """
        if k < 1:
            return 0
        n = len(prices)
        if k > n // 2:
            return self.solution_2(prices, n)
        dp = [[0] * 2 for _ in range(k)]
        for i in range(k):
            dp[i][0] = float('-inf')
        for p in prices:
            dp[0][0] = max(dp[0][0], -p)
            dp[0][1] = max(dp[0][1], dp[0][0] + p)
            for i in range(1, k):
                dp[i][0] = max(dp[i][0], dp[i - 1][1] - p)
                dp[i][1] = max(dp[i][1], dp[i][0] + p)
        return dp[k - 1][1]

    @staticmethod
    def solution_2(prices, n):
        res = 0
        for i in range(n - 1):
            diff = prices[i + 1] - prices[i]
            if diff > 0:
                res += diff
        return res
