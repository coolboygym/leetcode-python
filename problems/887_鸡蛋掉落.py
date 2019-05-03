"""
经典dp问题
参考：https://leetcode.com/problems/super-egg-drop/discuss/159079/Python-DP-from-kn2-to-knlogn-to-kn
"""

"""
暴力dp
dp有两个状态，鸡蛋的数量K与楼层的高度N
解决dp，我们需要找到子父问题之间的关联以及最小子问题的答案。

最小的子问题是什么？
从两个状态K与N来思考
1、如果只有1个鸡蛋，N层楼，则需要走N次。
2、如果有K的鸡蛋，1层楼，则需要走1次。

子父问题间的关联是什么？
dp[k][n] = min(max(dp[k-1][i-1],dp[k][n-i])+1 i=1..n)
有两种情况，
如果鸡蛋在第i层碎了，则剩下k-1的蛋和i-1层；如果鸡蛋在第i层没碎，则还有k个蛋和n-i层。

我们知道了dp状态转移关系和最小的子问题，可以自底向上地计算出dp数组。
以下是网友的解答。
"""


class Solution(object):
    def superEggDrop(self, K, N):
        """
        :type K: int
        :type N: int
        :rtype: int
        """
        dp = [[float('inf')] * (N + 1) for _ in range(K + 1)]
        # 构建基础子问题
        for i in range(1, K + 1):
            dp[i][0] = 0
            dp[i][1] = 1
        for j in range(1, N + 1):
            dp[1][j] = j

        # 自底向上地计算dp，O(KN^2)
        for i in range(2, K + 1):
            for j in range(2, N + 1):
                for k in range(1, j + 1):
                    dp[i][j] = min(dp[i][j], 1 + max(dp[i - 1][k - 1], dp[i][j - k]))
        return dp[K][N]


"""
以上方式算法复杂度过高，无法通过。
优化1
简化子父问题的关联。

比如说有10层，k个蛋
dp[k][10] = min(max(dp[k-1][0],dp[k][10])+1，max(dp[k-1][1],dp[k][9])+1，max(dp[k-1][2],dp[k][8])+1 i=1..n)
f1(i) = dp[k-1][i]递增函数
f2(i) = dp[k][n-i]递减函数

我们在求f1和f2在每个楼层i的最大值。能不能少算一些？
f1(i)>f2(i) max(f1,f2) = f1; f1(i)<f2(i) max(f1,f2) = f2
min(max(f1(i),f2(i)),....) 是f1(i)和f2(i)的交汇处。
详情见图 
https://leetcode.com/problems/super-egg-drop/solution/

以下是网友自顶向下的解法。O(KNlogN)
"""


class Solution2(object):
    def superEggDrop(self, K, N):
        memo = {}

        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    ans = 0
                elif k == 1:
                    ans = n
                else:
                    lo, hi = 1, n
                    # keep a gap of 2 X values to manually check later
                    while lo + 1 < hi:
                        x = (lo + hi) / 2
                        t1 = dp(k - 1, x - 1)
                        t2 = dp(k, n - x)

                        if t1 < t2:
                            lo = x
                        elif t1 > t2:
                            hi = x
                        else:
                            lo = hi = x

                    ans = 1 + min(max(dp(k - 1, x - 1), dp(k, n - x))
                                  for x in (lo, hi))

                memo[k, n] = ans
            return memo[k, n]

        return dp(K, N)


"""
O(KN)
"""


class Solution3(object):
    def superEggDrop(self, K, N):

        # Right now, dp[i] represents dp(1, i)
        dp = range(N + 1)

        for k in range(2, K + 1):
            # Now, we will develop dp2[i] = dp(k, i)
            dp2 = [0]
            x = 1
            for n in range(1, N + 1):
                # Let's find dp2[n] = dp(k, n)
                # Increase our optimal x while we can make our answer better.
                # Notice max(dp[x-1], dp2[n-x]) > max(dp[x], dp2[n-x-1])
                # is simply max(T1(x-1), T2(x-1)) > max(T1(x), T2(x)).
                while x < n and max(dp[x - 1], dp2[n - x]) > \
                        max(dp[x], dp2[n - x - 1]):
                    x += 1

                # The final answer happens at this x.
                dp2.append(1 + max(dp[x - 1], dp2[n - x]))

            dp = dp2

        return dp[-1]
