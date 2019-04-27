class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # 先判断是否存在 然后用dfs回溯
        res = []

        def wordBreak():
            dp = [False] * (len(s) + 1)
            dp[0] = True
            for i in range(len(s) + 1):
                if not dp[i]:
                    continue
                for word in wordDict:
                    if i + len(word) <= len(s) and s[i:i + len(word)] == word:
                        dp[i + len(word)] = True
            return dp[len(s)]

        if not wordBreak():
            return res

        def dfs(word, pos, tmp):
            tmp.append(word)
            pos += len(word)
            if len(s) == pos:
                res.append(" ".join(tmp[1:]))
            for w in wordDict:
                if pos + len(w) <= len(s) and s[pos:pos + len(w)] == w:
                    dfs(w, pos, tmp)
            tmp.pop()

        dfs("", 0, list())
        return res
