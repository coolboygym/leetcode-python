class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 遍历 + 双指针 不断更新当前最接近的三数之和 如果和等于目标值则直接返回
        nums.sort()
        close_sum = nums[0] + nums[1] + nums[2]
        size = len(nums)
        for i in range(0, size - 2):
            l = i + 1
            r = size - 1
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                if abs(target - three_sum) < abs(target - close_sum):
                    close_sum = three_sum
                if three_sum == target:
                    return target
                elif three_sum < target:
                    l += 1
                else:
                    r -= 1
        return close_sum


if __name__ == '__main__':
    s = Solution()
    assert s.threeSumClosest([-1, 2, 1, -4], 1) == 2
