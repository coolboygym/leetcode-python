class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 带限制条件的子集生成问题
        # 条件是：已有的右括号数目不能超过左括号
        if n == 0:
            return []
        res = [('', 0)]

        # 总共有n对括号 也就是会有n个左括号
        for i in range(2 * n):
            temp = []
            for r, c in res:
                if c > 0:
                    temp.append((r + ')', c - 1))
                if c <= n:
                    temp.append((r + '(', c + 1))
            res = temp
        return [x[0] for x in res if x[1] == 0]


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(1))
