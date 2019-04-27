class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    self.dfs(grid, i, j)
        return res

    def dfs(self, grid, i, j):
        grid[i][j] = 0
        if i > 0 and grid[i - 1][j] == '1':
            self.dfs(grid, i - 1, j)
        if i < len(grid) - 1 and grid[i + 1][j] == '1':
            self.dfs(grid, i + 1, j)
        if j > 0 and grid[i][j - 1] == '1':
            self.dfs(grid, i, j - 1)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == '1':
            self.dfs(grid, i, j + 1)


class Solution1(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 经典的DFS解法 考试要考的哦
        if not grid:
            return 0
        res = 0
        l, w = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i > l - 1 or j < 0 or j > w - 1 or grid[i][j] == '0':
                pass
            else:
                grid[i][j] = '0'
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        for i in range(l):
            for j in range(w):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i, j)
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.numIslands(
        [["1", "1", "1", "1", "0"],
         ["1", "1", "0", "1", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "0", "0", "0"]]) == 1
