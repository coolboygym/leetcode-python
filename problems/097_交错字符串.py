class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        # 经典动态规划 类比编辑距离的解法 根据状态转移方程把dp矩阵依次填满即可
        m, n, l = len(s1), len(s2), len(s3)
        if m + n != l:
            return False

        # dp[i][j]表示s3[0..i+j-1]能否由s1[0..i-1]和s2[0..j-1]交错得到
        dp = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and (s1[i - 1] == s3[i - 1])
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and (s2[j - 1] == s3[j - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (s3[i + j - 1] == s1[i - 1] and dp[i - 1][j]) or (
                    s3[i + j - 1] == s2[j - 1] and dp[i][j - 1])

        return dp[m][n]
