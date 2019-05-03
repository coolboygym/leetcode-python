# 单调队列问题

# 496. Next Greater Element I
# 503. Next Greater Element II
# 84.  Largest Rectangle in Histogram
# 122. Best Time to Buy and Sell Stock II
# 862. Shortest Subarray with Sum at Least K

# 寻找下一个更大的数

class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        mapping = [0] * len(T)

        # stack中分别存储每一个元素的下标和值
        stack = []
        for i in range(len(T)):
            while stack and T[i] > stack[-1][1]:
                top_idx, top_value = stack.pop()
                mapping[top_idx] = i - top_idx  # 使用下标计算相差的天数
            stack.append((i, T[i]))
        return mapping


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
