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


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('2'))
    print(s.letterCombinations('23'))

