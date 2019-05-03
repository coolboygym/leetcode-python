class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 详见博客: https://zhuanlan.zhihu.com/p/64377940
        n = len(height)
        if n <= 2:
            return 0

        # 寻找最高的柱子
        max_height = height[0]
        max_idx = 0
        for i in range(1, n):
            if height[i] > max_height:
                max_height = height[i]
                max_idx = i

        # 从左右两边分别朝最高的柱子遍历
        res = 0
        max_height_left = 0
        for i in range(max_idx):
            max_height_left = max(height[i], max_height_left)
            res += (max_height_left - height[i])
        max_height_right = 0
        for i in range(n - 1, max_idx, -1):
            max_height_right = max(height[i], max_height_right)
            res += (max_height_right - height[i])

        return res


class Solution1(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 一次遍历 借助集合的交并补思想
        n = len(height)
        area = 0
        max_height_left, max_height_right = 0, 0
        for i in range(n):
            max_height_left = max(max_height_left, height[i])
            max_height_right = max(max_height_right, height[-i - 1])
            area = area + max_height_left + max_height_right - height[i]
        return area - n * max_height_left
