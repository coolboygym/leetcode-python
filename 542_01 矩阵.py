class Solution:
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        self.m = len(matrix)
        self.n = len(matrix[0])
        res = [[0 for _ in range(self.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(self.n):
                res[i][j] = self.distance(i, j, 0, matrix, [])
        return res

    def distance(self, i, j, step, matrix, que):
        que.append((i, j, step))
        while que:
            temp = que.pop(0)
            if matrix[temp[0]][temp[1]] == 0:
                return temp[2]
            if temp[0] > 0:
                que.append((temp[0] - 1, temp[1], temp[2] + 1))
            if temp[1] > 0:
                que.append((temp[0], temp[1] - 1, temp[2] + 1))
            if temp[0] < self.m - 1:
                que.append((temp[0] + 1, temp[1], temp[2] + 1))
            if temp[1] < self.n - 1:
                que.append((temp[0], temp[1] + 1, temp[2] + 1))
