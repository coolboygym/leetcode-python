class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # 在二维矩阵上按照和递增顺序遍历 同时记录每个格子是否被访问过
        import heapq
        h = []
        n = len(matrix)
        if n == 0 or k == 0:
            return 0
        s = 1
        visited = set()
        heapq.heappush(h, (matrix[0][0], 0, 0))
        visited.add((0, 0))
        while s < k:
            item = heapq.heappop(h)
            i, j = item[1], item[2]
            if i < n - 1 and (i + 1, j) not in visited:
                heapq.heappush(h, (matrix[i + 1][j], i + 1, j))
                visited.add((i + 1, j))
            if j < n - 1 and (i, j + 1) not in visited:
                heapq.heappush(h, (matrix[i][j + 1], i, j + 1))
                visited.add((i, j + 1))
            s += 1

        return heapq.heappop(h)[0]


class Solution1(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import heapq
        n = len(matrix)
        if n == 0 or k == 0:
            return 0

        h = [(matrix[x][0], x, 0) for x in range(n)]
        heapq.heapify(h)
        for i in range(k - 1):
            item = heapq.heappop(h)
            i, j = item[1], item[2]
            if j < n - 1:
                heapq.heappush(h, (matrix[i][j + 1], i, j + 1))

        return heapq.heappop(h)[0]
