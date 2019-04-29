class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 总共要走m+n-2步 其中m-1步向下 n-1步向右 转化为排列组合问题
        N = m + n - 2
        M = m - 1 if m < n else n - 1
        res = 1
        for i in range(N - M + 1, N + 1):
            res *= i
        for i in range(1, M + 1):
            res /= i
        return res


class Solution1(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 经典的动态规划
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
