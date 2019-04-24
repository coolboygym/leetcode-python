class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 模拟行走的过程 注意初始化二维数组应该用列表生成式 如果用列表乘法只是复制了reference
        res = [[0 for _ in range(n)] for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for num in range(1, n * n + 1):
            res[i][j] = num
            if res[(i + di) % n][(j + dj) % n] != 0:
                di, dj = dj, -di
            i += di
            j += dj
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(3))
