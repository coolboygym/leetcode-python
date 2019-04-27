from functools import lru_cache


class Solution1:
    @lru_cache(10 ** 8)
    def climbStairs(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        # 借助LRU缓存保存中间结果 相当精彩
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution:
    def climbStairs(self, n: int) -> int:
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
