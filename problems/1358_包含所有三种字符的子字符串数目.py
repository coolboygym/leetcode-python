from collections import defaultdict
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = left = 0
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
            while len(cnt) == 3:
                out = s[left]  # 离开窗口的字母
                cnt[out] -= 1
                if cnt[out] == 0:
                    del cnt[out]
                left += 1
            ans += left
        return ans