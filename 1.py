class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = dict()
        for i in range(len(nums)):
            element = target - nums[i]
            element_index = mapping.get(element)
            if element_index is not None:
                return [element_index, i]
            else:
                mapping[nums[i]] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    res = solution.twoSum(nums, target)
    print(res)
