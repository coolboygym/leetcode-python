class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 一次遍历 不断更新当前最长子串的起点和终点
        # 参考链接: https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/comments/2558
        indexes = dict()
        result = 0
        start, end = 0, 0
        for i, char in enumerate(s):
            end = i
            if char in indexes:
                start = max(indexes[char] + 1, start)
            indexes[char] = i
            result = max(end - start + 1, result)
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abba") == 2
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
