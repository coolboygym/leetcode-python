class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        参考链接：https://leetcode-cn.com/problems/multiply-strings/comments/

        num1的第i位(高位从0开始)和num2的第j位相乘的结果在乘积中的位置是[i+j, i+j+1]
        例: 123 * 45,  123的第1位 2 和45的第0位 4 乘积 08 存放在结果的第[1, 2]位中
          index:    0 1 2 3 4

                        1 2 3
                    *     4 5
                    ---------
                          1 5
                        1 0
                      0 5
                    ---------
                      0 6 1 5
                        1 2
                      0 8
                    0 4
                    ---------
                    0 5 5 3 5
        这样我们就可以单独都对每一位进行相乘计算把结果存入相应的index中
        """
        n1, n2 = len(num1), len(num2)
        mul = [0] * (n1 + n2)
        zero = ord('0')
        for i in range(n1 - 1, -1, -1):
            for j in range(n2 - 1, -1, -1):
                temp = (ord(num1[i]) - zero) * (ord(num2[j]) - zero)

                # 举个例子来记：9加8等于17写7进1
                temp += mul[i + j + 1]
                mul[i + j] += temp // 10
                mul[i + j + 1] = temp % 10

        # 去除前导0
        i = 0
        while i < len(mul) - 1 and mul[i] == 0:
            i += 1

        res = ''.join([chr(x + zero) for x in mul[i:]])
        return res
