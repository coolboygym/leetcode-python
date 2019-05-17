class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        检查数字i是否在nums[i-1]的位置。
        O(N)
        """
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[nums[i] - 1] == nums[i]:
                    return nums[i]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]


class Solution2(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        二分法，子问题
        O(NlogN)
        """
        l = 1
        h = len(nums)
        while l < h:
            m = (l + h) // 2
            cnt = 0
            duplicate = 0
            for i in range(len(nums)):
                if nums[i] < m:
                    cnt += 1
                if nums[i] == m:
                    duplicate += 1
            if duplicate > 1:
                return m
            if cnt > m - 1:
                h = m
            else:
                l = m
        return l
