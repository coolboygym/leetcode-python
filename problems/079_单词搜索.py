class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # DFS
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board, i, j, word, 0):
                    return True
        return False

    def dfs(self, board, i, j, word, k):
        if k == len(word):
            return True
        m, n = len(board), len(board[0])

        # 判断下标是否越界 若未越界 还需对应字符相同才能继续往下查找
        if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
            return False
        temp = board[i][j]

        # 标记节点已被访问
        board[i][j] = '*'

        # 每次都往四个方向搜索 把下标是否越界的判断留给子调用自己来做
        res = self.dfs(board, i + 1, j, word, k + 1) or self.dfs(
            board, i - 1, j, word, k + 1) or self.dfs(
            board, i, j + 1, word, k + 1) or self.dfs(board, i, j - 1, word, k + 1)

        # 回溯
        board[i][j] = temp
        return res
