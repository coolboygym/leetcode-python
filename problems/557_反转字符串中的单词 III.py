class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, n = 0, len(s)
        res = [x for x in s]
        while i < n:
            j = i + 1

            # 找到下一个空格所在位置
            while j < n and s[j] != ' ':
                j += 1

            # 双指针翻转单词
            l, r = i, j - 1
            while l < r:
                res[l], res[r] = res[r], res[l]
                l += 1
                r -= 1

            # 将i设置为下一个单词的起始位置
            i = j + 1

        return ''.join(res)

