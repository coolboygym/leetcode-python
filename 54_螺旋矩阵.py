class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 模拟行走的过程 将走过的地方做标记 如果下一步已经走过则调转方向
        # di, dj = dj, -di 这一步可以通过实例找规律得到
        res, i, j, di, dj = [], 0, 0, 0, 1
        if matrix:
            m, n = len(matrix), len(matrix[0])
            for _ in range(m * n):
                res.append(matrix[i][j])
                matrix[i][j] = None
                if matrix[(i + di) % m][(j + dj) % n] is None:
                    di, dj = dj, -di
                i += di
                j += dj
        return res
