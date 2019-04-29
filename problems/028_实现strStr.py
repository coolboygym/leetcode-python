class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # 朴素解法 时间复杂度O(m*n)
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


class Solution1(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        if not haystack:
            return -1

        # 手动实现KMP算法
        # 参考链接: https://www.cnblogs.com/yjiyjige/p/3263858.html
        next_array = self.getNext(needle)
        i, j = 0, 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next_array[j]
        if j == len(needle):
            return i - j
        else:
            return -1

    def getNext(self, pattern):
        n = len(pattern)
        next_array = [0] * n
        next_array[0] = -1
        k = -1
        j = 0
        while j < n - 1:
            if k == -1 or pattern[k] == pattern[j]:
                k += 1
                j += 1
                if pattern[k] == pattern[j]:
                    next_array[j] = next_array[k]
                else:
                    next_array[j] = k
            else:
                k = next_array[k]
        return next_array


if __name__ == '__main__':
    s = Solution()
    assert s.strStr('hello', 'll') == 2
    assert s.strStr('aaaaa', 'bba') == -1
    assert s.strStr('', '') == 0
    assert s.strStr('ab', 'ab') == 0
