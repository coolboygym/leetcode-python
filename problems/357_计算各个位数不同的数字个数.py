class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 因为n只能小于10 所以直接写答案
        results = [1, 10, 91, 739, 5275, 32491, 168571, 712891, 2345851, 5611771, 8877691]
        return results[n]


class Solution1(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # DFS的变型
        return self.doCount(n, [False for _ in range(10)], 0)

    def doCount(self, n, used, depth):
        if depth == n:
            return 1
        total = 1
        start = 1 if depth == 0 else 0
        for i in range(start, 10):
            if not used[i]:
                used[i] = True
                total += self.doCount(n, used, depth + 1)
                used[i] = False
        return total


class Solution2(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 经典的动态规划解法 每次在之前的基础上增加一位数字
        # 如果之前的数字是k位 为了保证不重复 新增的一位只有10-k种选择
        if n == 0:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 10
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + (dp[i - 1] - dp[i - 2]) * (10 - (i - 1))
        return dp[n]
