class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 遍历整个数独 对每个数判断它所在的行、列以及子宫格中是否已经出现过该数
        # 若是直接返回False 否则遍历结束后返回True
        # 元素对应的子宫格id的计算可以用实例推导下
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        boxes = [{} for _ in range(9)]
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != '.':
                    num = int(num) - 1
                    box_idx = (i // 3) * 3 + j // 3
                    rows[i][num] = rows[i].get(num, 0) + 1
                    cols[j][num] = cols[j].get(num, 0) + 1
                    boxes[box_idx][num] = boxes[box_idx].get(num, 0) + 1
                    if rows[i][num] > 1 or cols[j][num] > 1 or boxes[box_idx][num] > 1:
                        return False
        return True
