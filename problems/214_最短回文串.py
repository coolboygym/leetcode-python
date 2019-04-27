class Solution:
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ss = s[::-1]
        n = len(ss)

        # 这里end=-1是为了保证局部变量i在访问前被赋值 否则输入为空的话会报错
        for i in range(len(s), -1, -1):
            if ss[n - i:] == s[:i]:
                break

        return ss[:n - i] + s
