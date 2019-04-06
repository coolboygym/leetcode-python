import functools


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        # 巧用自定义的字典排序
        def cmp(str1, str2):
            if str1 + str2 > str2 + str1:
                return 1
            else:
                return -1

        res = ''.join(sorted([str(num) for num in nums], key=functools.cmp_to_key(cmp), reverse=True))
        # 去除前导0
        i = 0
        while i < len(res) - 1 and res[i] == '0':
            i += 1
        return res[i:]


if __name__ == '__main__':
    s = Solution()
    print(s.largestNumber([10, 2]))
    print(s.largestNumber([3, 30, 34, 5, 9]))
    print(s.largestNumber([0, 0]))
