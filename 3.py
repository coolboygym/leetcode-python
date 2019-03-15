class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contents = dict()
        result = 0
        start, end = 0, 0
        for i, char in enumerate(s):
            end = i
            if char in contents:
                start = max(contents[char] + 1, start)
            contents[char] = i
            result = max(end - start + 1, result)
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.lengthOfLongestSubstring("abba") == 2
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
