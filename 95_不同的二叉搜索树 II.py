# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        """
        朴素递归法会存在重复计算区间，比如：
        计算[1,5]会需要计算[1,3]
        计算[1,6]也会计算[1,3] 这部分可以进行缓存：如果区间已经初始化过，直接使用即可
        """
        if not n:
            return []
        # 不知道为啥这里写n+1的话网站上运行会报错 可能是力扣的bug吧
        dp = [[[] for _ in range(n + 2)] for _ in range(n + 2)]
        self.build(1, n, dp)
        return dp[1][n]

    def build(self, start, end, dp):
        if len(dp[start][end]) != 0:
            return
        # start>end 说明上次调用时start=end 也就是只有一个节点 所以这里生成一个None作为子节点
        if start > end:
            dp[start][end].append(None)
        for i in range(start, end + 1):
            self.build(start, i - 1, dp)
            self.build(i + 1, end, dp)
            for l in dp[start][i - 1]:
                for r in dp[i + 1][end]:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    dp[start][end].append(root)
