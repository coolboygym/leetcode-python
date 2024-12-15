class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        ### 标准的定长滑动窗口三步走
        ans = curr = 0
        for i, char in enumerate(s):
            # 1. 新数据进入窗口
            if char in 'aeiou':
                curr += 1
            if i < k - 1:   # 不足窗口大小 初始的几个数据
                continue
            # 2. 更新答案
            ans = max(ans, curr)
            # 3. 老数据离开窗口
            if s[i - k + 1] in 'aeiou':
                curr -= 1
        return ans