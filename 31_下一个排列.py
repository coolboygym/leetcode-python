class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 对于有边界条件的题目 while 比 for 更直观
        n = len(nums)
        i = n - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i >= 0:
            j = n - 1
            while j >= i and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        self.reverse(nums, i + 1)

    @staticmethod
    def reverse(nums, start):
        i = start
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    s = Solution()
    print(s.nextPermutation([3, 1, 2]))
    print(s.nextPermutation([3, 1, 1]))
    print(s.nextPermutation([1, 3, 1]))
    print(s.nextPermutation([1, 1, 3]))
