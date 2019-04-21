class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        """
        动态规划 对于任意一天考虑四个变量:
        fstBuy: 在该天第一次买入股票可获得的最大收益 
        fstSell: 在该天第一次卖出股票可获得的最大收益
        secBuy: 在该天第二次买入股票可获得的最大收益
        secSell: 在该天第二次卖出股票可获得的最大收益
        分别对四个变量进行相应的更新, 最后secSell就是最大
        收益值(secSell >= fstSell)
        """
        firstBuy, secondBuy = float('-inf'), float('-inf')
        firstSell, secondSell = 0, 0
        for p in prices:
            firstBuy = max(firstBuy, -p)
            firstSell = max(firstSell, firstBuy + p)
            secondBuy = max(secondBuy, firstSell - p)
            secondSell = max(secondSell, secondBuy + p)

        return secondSell
