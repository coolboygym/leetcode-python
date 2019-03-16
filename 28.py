class Solution1(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0

        if haystack == '':
            return -1

        m, n, i = len(haystack), len(needle), 0
        while i < len(haystack) and m - i >= n:
            if haystack[i] == needle[0]:
                j = 0
                flag = True
                while j < n:
                    if haystack[i + j] != needle[j]:
                        flag = False
                        break
                    j += 1
                if flag:
                    return i
            i += 1
        return -1


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


if __name__ == '__main__':
    s = Solution()
    assert s.strStr('hello', 'll') == 2
    assert s.strStr('aaaaa', 'bba') == -1
    assert s.strStr('', '') == 0
    assert s.strStr('ab', 'ab') == 0
