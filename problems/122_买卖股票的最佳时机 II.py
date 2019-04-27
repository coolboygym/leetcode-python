class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 贪心法 只要今天比昨天高就卖出 因为你可以在同一天卖出再买入
        # 参考链接: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/comments/42837
        res = 0
        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            if diff > 0:
                res += diff
        return res
