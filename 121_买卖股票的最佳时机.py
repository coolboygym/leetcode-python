class Solution1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 贪心法 保存当前为止股票价格的最小值和最大收益
        # 或者由动态规划的角度理解：通过第i天 是/否 进行交易来决定状态转移方程
        if not prices:
            return 0
        res = 0
        min_val = prices[0]
        for price in prices[1:]:
            res = max(res, price - min_val)
            min_val = price if price < min_val else min_val
        return res


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 更加通用的解法 可以推广到123题
        firstBuy = float('-inf')
        firstSell = 0
        for p in prices:
            firstBuy = max(firstBuy, -p)
            firstSell = max(firstSell, firstBuy + p)
        return firstSell
