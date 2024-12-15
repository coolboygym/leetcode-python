from collections import Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # 标准定长滑窗 使用两个计数器
        n = len(s)
        ans = 0
        window = s[:minSize]
        char_count = Counter(window)
        str_count = Counter()
        if len(char_count) <= maxLetters:
            str_count[window] += 1
            ans = 1
        for i in range(minSize, n):
            char_count[window[0]] -= 1
            if char_count[window[0]] == 0:
                del char_count[window[0]]
            window = window.replace(window[0], '', 1)
            
            window = window + s[i]
            char_count[s[i]] += 1
            if len(char_count) <= maxLetters:
                str_count[window] += 1
                ans = max(ans, str_count[window])
        return ans


class Solution1:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # 网友解法 使用一个滑窗 执行时间居然比上面的方法快很多
        # 给出一个窗口，窗口的范围是min和max
        # 窗口满足要求字母重复次数小于等于maxletters
        cnt = Counter()
        n = len(s)
        for i in range(0,n-minSize+1):
            # 如果子串重复出现，该子串内的子串必然重复出现，故统计子串内最小即可
            j = i + minSize
            cnt[s[i:j]] += 1
        for j in cnt.keys():
            if len(set(j)) > maxLetters:
                cnt[j] = 0
        return max(cnt.values())
