"""
例 A = [2,-1,2,1]，K=3

此处有两种方式，一种sum(A[0:3]) = 3，一种sum(A[2:4]) = 3
输出最短的子数组4-2 = 2

方法参考：https://leetcode.com/articles/shortest-subarray-with-sum-atleast-k/

单调队列的解法

首先我们先计算前i-1个数的和，并存入P[i]

P = [0,2,1,3,4]
可以看到P[3]-P[0] = 3, P[4]-P[2] = 3
愿问题转化为P[b]-P[a]>=k的最小b-a

发现1：假设存在下标a1,b1满足条件，如果有a2>a1且P[a2]<P[a1]，则a2,b1更优。
发现2：假设存在下标a1,b1满足条件，又有b2>b1也满足条件，b1已经是最优解，因为b2-a1>b1-a1。
"""


class Solution(object):
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        P = [0]

        for x in A:
            P.append(P[-1] + x)

        stack = []
        ans = len(P)
        for b in range(len(P)):
            while stack and P[b] < stack[-1][-1]:
                stack.pop()

            while stack and P[b] - stack[0][-1] >= K:
                a, _ = stack.pop(0)
                ans = min(ans, b - a)

            stack.append((b, P[b]))

        return ans if ans < len(P) else -1


if __name__ == '__main__':
    s = Solution()
    print(s.shortestSubarray([2, -1, 2, 1], 3))
