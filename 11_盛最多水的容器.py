class Solution2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        max_area = min(height[i], height[j]) * j
        while i < j:
            if height[i] < height[j]:
                i += 1
                curr_area = min(height[i], height[j]) * (j - i)
                if curr_area > max_area:
                    max_area = curr_area
            else:
                j -= 1
                curr_area = min(height[i], height[j]) * (j - i)
                if curr_area > max_area:
                    max_area = curr_area
        return max_area


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 参考快速排序的写法
        i = 0
        j = len(height) - 1
        max_area = min(height[i], height[j]) * j
        while i < j:
            while i < j and height[i] < height[j]:
                max_area = max(max_area, height[i] * (j - i))
                i += 1
            while i < j and height[i] >= height[j]:
                max_area = max(max_area, height[j] * (j - i))
                j -= 1
        return max_area
