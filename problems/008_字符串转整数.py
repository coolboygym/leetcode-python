import re


class Solution:
    def myAtoi(self, str: str) -> int:
        a = re.sub('\d*-', '-', ''.join(re.findall(r'^[-+]{0,1}\d+', str.strip())))
        if not a:
            return 0
        a = int(a)
        b = 2 ** 31
        if a > b - 1:
            return b - 1
        elif a < -b:
            return -b
        else:
            return a


if __name__ == '__main__':
    s = Solution()
    assert s.myAtoi('123 345 www 234') == 123
