class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 以右上角作为参考点 一次排除一行或一列 时间复杂度O(m+n)
        # 虽然不如二分查找效率高 但代码简洁、不容易出错
        m = len(matrix)
        if m == 0:
            return False
        row = 0
        col = len(matrix[0]) - 1
        while row < m and col >= 0:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True
        return False
