class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        n = len(nums)
        left, right, length = 0, 1, 0
        for i in range(n):
            right = len(res)
            if i != 0 and nums[i] == nums[i - 1]:
                left = right - length
            else:
                left = 0
            length = right - left

            for j in range(left, right):
                temp = res[j].copy()
                temp.append(nums[i])
                res.append(temp)
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.subsetsWithDup([1, 1]))
