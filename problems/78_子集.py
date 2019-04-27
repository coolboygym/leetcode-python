class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = pow(2, m)
        i = 0
        res = []
        while i < n:
            temp = []
            j = 0
            while j < m:
                s = 1 << j
                if s & i:
                    temp.append(nums[j])
                j += 1
            i += 1
            res.append(temp)
        return res


class Solution1(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            size = len(result)
            for i in range(size):
                a = result[i].copy()
                a.append(num)
                result.append(a)
        return result


class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        for num in nums:
            new_ones = [x.copy() for x in result]
            for item in new_ones:
                item.append(num)
            result.extend(new_ones)
        return result


if __name__ == '__main__':
    solution = Solution()
    assert solution.subsets([1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
