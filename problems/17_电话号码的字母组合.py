class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 子集问题
        if digits == '':
            return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = ['']
        size = len(digits)
        for i in range(size):
            temp = []
            for j in (mapping[digits[i]]):
                for r in res:
                    temp.append(r + j)
            res = temp
        return res


class Solution1(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 看做图论问题 采用深度优先搜索 递归遍历
        if not digits:
            return []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        res = []
        self.dfs(res, '', digits, mapping, 0)
        return res

    def dfs(self, result, string, digits, mapping, k):
        if len(string) == len(digits):
            result.append(string)
            return

        chars = mapping[digits[k]]
        for char in chars:
            string += char
            self.dfs(result, string, digits, mapping, k + 1)
            string = string[:-1]


if __name__ == '__main__':
    s = Solution()
    assert s.letterCombinations('2') == ['a', 'b', 'c']
    assert s.letterCombinations('23') == ['ad', 'bd', 'cd', 'ae', 'be', 'ce', 'af', 'bf', 'cf']
