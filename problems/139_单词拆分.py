class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 完全背包问题
        # 朴素递归 包含重复计算 超出时间限制
        if not s:
            return True

        for word in wordDict:
            if s.startswith(word):
                flag = self.wordBreak(s[len(word):], wordDict)
                if flag:
                    return True
        return False


class Solution1(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 动态规划 dp[i]表示s的前i个字符能否拆成wordDict中的单词
        dp = [False for _ in range(len(s) + 1)]
        # 遍历s的所有子串
        for i in range(1, len(s) + 1):
            # 前i个字符在字典里 直接返回True
            if s[:i] in wordDict:
                dp[i] = True
                continue
            # 将前i个字符分成两部分 当且仅当两部分都满足时才满足
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[len(s)]
