class Solution:
    def minSizeSubarray(self, nums: list[int], target: int) -> int:
        # 转化为求长度为2n的数组里的最短子数组
        # 最后返回结果再加上K倍的_sum
        _sum = sum(nums)
        n = len(nums)
        _target = target % _sum
        ans = n * 2
        left = curr_sum = 0
        for right in range(n * 2):
            curr_sum += nums[right % n]
            while curr_sum > _target:
                curr_sum -= nums[left % n]
                left += 1
            if curr_sum == _target:
                ans = min(ans, right - left + 1)
        return ans + target // _sum * n if ans < n * 2 else -1