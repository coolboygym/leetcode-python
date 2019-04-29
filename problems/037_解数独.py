class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # DFS回溯
        # rows: 某一行某个数是否出现过
        # cols: 某一列某个数是否出现过
        # boxes: 某个子宫格中某个数是否出现过
        rows = [[False for _ in range(9)] for _ in range(9)]
        cols = [[False for _ in range(9)] for _ in range(9)]
        boxes = [[False for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    box_idx = i // 3 * 3 + j // 3
                    rows[i][num] = True
                    cols[j][num] = True
                    boxes[box_idx][num] = True
        self.dfs(board, rows, cols, boxes, 0, 0)

    def dfs(self, board, rows, cols, boxes, i, j):
        # 找到下一个待填充位置
        while board[i][j] != '.':
            j += 1
            if j == 9:
                i += 1
                j = 0
            # 如果未找到说明全部都已空格正确填充 返回True
            if i == 9:
                return True

        # 逐一尝试该位置是否可以放入
        for num in range(9):
            box_idx = i // 3 * 3 + j // 3

            # 在对应的行、列、子宫格中该数都未出现过 当前可以填入
            if not rows[i][num] and not cols[j][num] and not boxes[box_idx][num]:
                board[i][j] = str(1 + num)
                rows[i][num] = True
                cols[j][num] = True
                boxes[box_idx][num] = True

                # DFS递归填充下一个空格
                if self.dfs(board, rows, cols, boxes, i, j):
                    return True

                # 如果递归失败说明当前方案不可行 需要修改本次填充的值 进行回溯
                else:
                    rows[i][num] = False
                    cols[j][num] = False
                    boxes[box_idx][num] = False
                    board[i][j] = '.'
        return False
