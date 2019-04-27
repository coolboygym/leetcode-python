class Solution1(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 搜索循环有序数组 经典的二分查找的变型
        # 循环有序数组从中间某处切分开后 得到一个有序数组和一个循环有序数组
        # 下一次的寻找只需要在其中某一部分继续进行
        return self.help(nums, 0, len(nums) - 1, target)

    def help(self, nums, low, high, target):
        if low > high:
            return -1
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid

        if nums[mid] < nums[high]:
            if nums[mid] < target <= nums[high]:
                return self.help(nums, mid + 1, high, target)
            else:
                return self.help(nums, low, mid - 1, target)
        else:
            if nums[low] <= target < nums[mid]:
                return self.help(nums, low, mid - 1, target)
            else:
                return self.help(nums, mid + 1, high, target)


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 也可以用while来实现
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] == target:
                return mid

            if nums[mid] < nums[high]:  # 右半部分是有序的
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

        return -1
