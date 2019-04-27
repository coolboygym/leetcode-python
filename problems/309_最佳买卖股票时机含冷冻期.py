class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        参考链接: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/comments/10290
        sell[i]表示截至第i天，最后一个操作是卖时的最大收益；
        buy[i]表示截至第i天，最后一个操作是买时的最大收益；
        cool[i]表示截至第i天，最后一个操作是冷冻期时的最大收益；
        """
        n = len(prices)
        if n == 0:
            return 0
        sell = [0 for _ in range(n)]
        buy = [0 for _ in range(n)]
        cool = [0 for _ in range(n)]
        buy[0] = -prices[0]
        for i in range(1, n):
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
            buy[i] = max(cool[i - 1] - prices[i], buy[i - 1])
            cool[i] = sell[i - 1]
        return sell[-1]
