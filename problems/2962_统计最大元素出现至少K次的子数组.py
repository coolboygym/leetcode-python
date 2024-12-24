from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        m = max(nums)
        ans = left = 0
        cnt = defaultdict(int)
        for x in nums:
            cnt[x] += 1
            while cnt[m] >= k:
                out = nums[left]    # 离开窗口的元素
                cnt[out] -= 1
                left += 1
            ans += left
        return ans