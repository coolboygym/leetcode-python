class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        ans = 0
        left = 0
        n = len(s)
        costs = [0] * n
        for i in range(n):
            costs[i] = abs(ord(s[i]) - ord(t[i]))
        curr_sum = 0
        for right, x in enumerate(s):
            curr_sum += costs[right]
            while curr_sum > maxCost:
                curr_sum -= costs[left]
                left += 1
            ans = max(ans, right - left + 1)
        return ans