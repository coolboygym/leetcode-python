class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 三路快排
        i, j, k = 0, len(nums) - 1, 0
        while k < len(nums):
            if nums[k] == 0 and k > i:
                nums[k], nums[i] = nums[i], nums[k]
                i += 1
            elif nums[k] == 2 and k < j:
                nums[k], nums[j] = nums[j], nums[k]
                j -= 1
            else:
                k += 1


if __name__ == '__main__':
    s = Solution()
    input_nums = [2, 0, 1]
    s.sortColors(input_nums)
    assert input_nums == [0, 1, 2]
