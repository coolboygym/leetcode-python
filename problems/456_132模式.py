class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 参考链接: https://leetcode-cn.com/problems/132-pattern/comments/9819
        # 贪心算法 记录最大值和次大值 寻找匹配的最小值
        # 直接用数组的append和pop操作就可以实现一个栈
        # 栈中保存的是第二个数的所有候选者
        stack = []
        num2 = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            # 当前数小于第二个数 也就是找到了第一个数 返回True
            if nums[i] < num2:
                return True
            # 如果当前的数大于候选者 则当前数可以作为第三个数
            # 不断更新第二个数 保证它和第三个数的差距最小 从而给找第一个数留出最大的空间
            while stack and nums[i] > stack[-1]:
                num2 = stack.pop()
            stack.append(nums[i])
        return False


if __name__ == '__main__':
    s = Solution()
    assert s.find132pattern([1, 2, 3, 4]) is False
    assert s.find132pattern([1, 3, 4, 2]) is True
