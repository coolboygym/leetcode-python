class Solution:
    def isPalindrome(self, s: str) -> bool:
        # filter关键字
        s = ''.join(filter(str.isalnum, s)).lower()
        return s == s[::-1]


class Solution1(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 双指针
        target_str = []
        for i in range(len(s)):
            if s[i].isalnum():
                target_str.append(s[i])
        target_str = ''.join(target_str).lower()
        i, j = 0, len(target_str) - 1
        while i < j:
            if target_str[i] != target_str[j]:
                return False
            i += 1
            j -= 1
        return True
