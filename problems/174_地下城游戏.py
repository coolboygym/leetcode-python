class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        # 参考：https://leetcode-cn.com/problems/dungeon-game/comments/88514
        # 按照逆序动态规划 增加边界简化判断
        # 无论何时骑士的健康点数都必须大于0
        m, n = len(dungeon), len(dungeon[0])
        cost = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        for i in range(m + 1):
            cost[i][n] = float('inf')
        for j in range(n + 1):
            cost[m][j] = float('inf')

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    cost[i][j] = 1 if dungeon[i][j] > 0 else 1 - dungeon[i][j]
                else:
                    cost[i][j] = max(1, min(cost[i + 1][j], cost[i][j + 1]) - dungeon[i][j])
        return cost[0][0]
