class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if not strs:
            return prefix
        for i in range(len(strs[0])):
            p = strs[0][i]
            for s in strs:
                if i >= len(s):
                    return prefix
                if s[i] != p:
                    return prefix
            prefix += p
        return prefix
