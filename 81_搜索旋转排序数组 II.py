class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        # 由于存在重复元素 因此无法直接根据low high mid三个数的大小关系判断哪边是递增 哪边是循环递增
        # 需要先对low和high做一下去重 这样保证剩下的元素可以按照常规的二分流程走
        low, high = 0, len(nums) - 1
        while low <= high:
            while low < high and nums[low] == nums[low + 1]:
                low += 1
            while low < high and nums[high] == nums[high - 1]:
                high -= 1

            mid = low + (high - low) // 2
            if nums[mid] == target:
                return True
            if nums[mid] < nums[high]:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
            else:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return False


if __name__ == '__main__':
    s = Solution()
    assert s.search([3, 1, 1], 3) is True
    assert s.search([1, 1, 3, 1], 3) is True
