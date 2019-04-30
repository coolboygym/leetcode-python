class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 经典动态规划
        m = len(word1)
        n = len(word2)

        # dp[i][j]表示从word1[0..i-1]到word2[0..j-1]的编辑距离 当i或j为0时表示其对应空串
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    # 当前字符相同 不需要做任何新的操作
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # 当前字符不同 min中三项分别对应替换、增加和删除
                    dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
