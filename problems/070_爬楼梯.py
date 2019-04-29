from functools import lru_cache


class Solution:
    @lru_cache(10 ** 8)
    def climbStairs(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        # 借助LRU缓存保存中间结果 相当精彩
        # 参考链接: https://leetcode-cn.com/problems/climbing-stairs/comments/4001
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution1:
    def climbStairs(self, n: int) -> int:
        # 尾递归可以转化为迭代
        if n == 1:
            return 1
        if n == 2:
            return 2

        res = 0
        n1, n2 = 1, 2
        for _ in range(3, n + 1):
            res = n1 + n2
            n1, n2 = n2, res

        return res
