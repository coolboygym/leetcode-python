class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        result = list()
        size = len(nums)
        for z in range(size):
            if z > 0 and nums[z] == nums[z - 1]:
                continue
            new_target = target - nums[z]

            for x in range(z + 1, size):
                if x > z + 1 and nums[x] == nums[x - 1]:
                    continue
                new_target2 = new_target - nums[x]

                i = x + 1
                j = size - 1
                while i < j:
                    temp_sum = nums[i] + nums[j]
                    if temp_sum == new_target2:
                        result.append([nums[z], nums[x], nums[i], nums[j]])
                        while i < j and nums[i] == nums[i + 1]:
                            i += 1
                        while i < j and nums[j] == nums[j - 1]:
                            j -= 1
                        i += 1
                        j -= 1
                    elif temp_sum < new_target2:
                        i += 1
                    else:
                        j -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2], 0))
    print(s.fourSum([0, 0, 0, 0], 0))
