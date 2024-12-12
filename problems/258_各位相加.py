class Solution0(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            num = str(num)
            temp = 0
            for char in num:
                temp += int(char)
            num = temp
        return num

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 数学分析后得 num与最终结果模9同余(最终结果也叫数根) 又知最终结果为1位数
        if num == 0:
            return num
        if num % 9 == 0:
            return 9
        return num % 9


if __name__ == '__main__':
    s = Solution()
    assert s.addDigits(38) == 2
    assert s.addDigits(99) == 9