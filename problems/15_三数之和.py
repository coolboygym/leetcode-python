class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 选出第一个数后转化为两数之和 对数组做排序方便过滤重复项 时间复杂度O(n^2)
        result = []
        size = len(nums)
        nums = sorted(nums)
        for z in range(size):
            if z > 0 and nums[z] == nums[z - 1]:
                continue
            new_target = 0 - nums[z]

            i = z + 1
            j = size - 1
            while i < j:
                temp_sum = nums[i] + nums[j]
                if temp_sum == new_target:
                    result.append([nums[z], nums[i], nums[j]])
                    while i < j and nums[i] == nums[i + 1]:
                        i += 1
                    while i < j and nums[j] == nums[j - 1]:
                        j -= 1
                    i += 1
                    j -= 1
                elif temp_sum < new_target:
                    i += 1
                else:
                    j -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    assert s.threeSum([1, 0, -1, 0, -2, 2]) == [[-2, 0, 2], [-1, 0, 1]]
    assert s.threeSum([0, 0, 0, 0]) == [[0, 0, 0]]
