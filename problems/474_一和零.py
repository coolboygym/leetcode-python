class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        size = len(strs)
        if size == 0:
            return 0

        # 初始化dp数组
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        # 遍历每一个字符串
        for s in strs:
            zeros = 0
            ones = 0
            for char in s:
                if char == '0':
                    zeros += 1
                else:
                    ones += 1
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    # 两种情况取最大值：不使用该字符串和使用该字符串
                    # 这里使用了滚动数组的技巧 每次遍历时dp中保存的是上一次遍历结束时的状态
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]
