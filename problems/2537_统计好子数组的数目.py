from collections import defaultdict

class Solution:
    def countGood(self, nums: list[int], k: int) -> int:
        # pairs是当前窗口内所有满足条件的下标对数量
        ans = left = 0
        cnt = defaultdict(int)
        pairs = 0
        for x in nums:
            pairs += cnt[x]
            cnt[x] += 1
            while pairs >= k:
                out = nums[left]
                cnt[out] -= 1
                pairs -= cnt[out]
                left += 1
            ans += left
        return ans