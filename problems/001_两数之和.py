class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 使用哈希表保存数字与其索引间的映射 通过一遍扫描解决
        mapping = dict()
        for i in range(len(nums)):
            element = target - nums[i]
            element_index = mapping.get(element)
            if element_index is not None:
                return [element_index, i]
            else:
                mapping[nums[i]] = i


if __name__ == '__main__':
    solution = Solution()
    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]
