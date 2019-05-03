# 暴力法O(N^2)

# 二分法O(NlogN)
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        def helper(i, j):
            if i > j:
                return 0
            if i == j:
                return heights[i]

            min_height = min(heights[i:j + 1])
            min_height_idx = heights[i:j + 1].index(min_height)
            return max(helper(i, i + min_height_idx - 1), helper(i + min_height_idx + 1, j), min_height * (j - i + 1))

        return helper(0, len(heights) - 1)


# 单调队列
class Solution2(object):
    def largestRectangleArea(self, height):
        height.append(0)
        stack = [-1]
        ans = 0
        for i in range(len(height)):
            while height[i] < height[stack[-1]]:
                h = height[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)
        height.pop()
        return ans


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    s = Solution()
    print(s.largestRectangleArea(heights))
