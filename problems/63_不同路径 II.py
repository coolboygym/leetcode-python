class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        """
        动态规划:
        1.障碍物所在点状态值dp[i][j]为0
        2.若障碍物在第一行或者第一列，则其后和其下所有的状态值都为0
        """
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(n):
            if obstacleGrid[0][i]:
                break
            else:
                dp[0][i] = 1

        for i in range(m):
            if obstacleGrid[i][0]:
                break
            else:
                dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
