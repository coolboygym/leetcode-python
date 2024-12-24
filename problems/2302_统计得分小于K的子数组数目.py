class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0
        ans = left = size = sums = 0
        for right, x in enumerate(nums):
            size += 1
            sums += x
            while size * sums >= k:
                size -= 1
                sums -= nums[left]
                left += 1
            ans += (right - left + 1)
        return ans