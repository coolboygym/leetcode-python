class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        n = len(s)
        left = 0
        ans = 1
        nums = 0
        for right in range(1, n):
            if s[right] == s[right-1]:
                nums += 1
            while nums > 1:
                if s[left] == s[left+1]:
                    nums -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans