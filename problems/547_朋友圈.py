class Solution1(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # DFS变型 根据数据的存储结构进行适当调整
        n = len(M)
        res = 0
        visited = [False for _ in range(n)]
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                self.dfs(M, visited, i)
                res += 1
        return res

    def dfs(self, matrix, visited, i):
        for j in range(i + 1, len(matrix)):
            if matrix[i][j] == 1 and not visited[j]:
                visited[j] = True
                self.dfs(matrix, visited, j)


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        # 经典的并查集解法
        n = len(M)
        parent = [i for i in range(n)]
        for i in range(n):
            for j in range(n):
                if M[i][j] == 1:
                    x = self.find_parent(parent, i)
                    y = self.find_parent(parent, j)
                    parent[y] = x
        res = 0
        for i in range(n):
            if parent[i] == i:
                res += 1
        return res

    def find_parent(self, parent, node):
        while node != parent[node]:
            node = parent[node]
        return node
