class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        ### 双指针不定长滑动窗口
        # k是限制条件 相当于可以用来修改的总成本
        nums.sort()
        n = len(nums)
        cost = 0
        l = 0
        ans = 1
        for r in range(1, n):
            # 在r进入窗口时 需要付出的成本
            cost += (nums[r] - nums[r-1]) * (r - l)
            while cost > k:
                # 在l退出窗口时 可以减少的成本
                cost -= (nums[r] - nums[l])
                l += 1
            ans = max(ans, r - l + 1)
        return ans