class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 一次遍历 不断更新当前最长子串的起点和终点
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
