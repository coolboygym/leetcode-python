class Solution0:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # 在while循环内更新ans
        n = len(nums)
        ans = n + 1  # 也可以写 inf
        s = left = 0
        for right, x in enumerate(nums):  # 枚举子数组右端点
            s += x
            while s >= target:  # 满足要求
                ans = min(ans, right - left + 1)
                s -= nums[left]
                left += 1  # 左端点右移
        return ans if ans <= n else 0


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # 在while循环结束后更新ans
        n = len(nums)
        ans = n + 1  # 也可以写 inf
        s = left = 0
        for right, x in enumerate(nums):  # 枚举子数组右端点
            s += x
            while s - nums[left] >= target:  # 尽量缩小子数组长度
                s -= nums[left]
                left += 1  # 左端点右移
            if s >= target:
                ans = min(ans, right-left+1)
        return ans if ans <= n else 0