class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if not nums:
            return []

        res = list()
        windows = list()
        for i in range(k):
            pos = self.binary_search(windows, nums[i])
            windows.insert(pos, nums[i])
        res.append((windows[k // 2] + windows[(k - 1) // 2]) / 2)

        for idx in range(k, len(nums)):
            pos = self.binary_search(windows, nums[idx - k])
            windows.pop(pos)
            pos = self.binary_search(windows, nums[idx])
            windows.insert(pos, nums[idx])
            res.append((windows[k // 2] + windows[(k - 1) // 2]) / 2)

        return res

    @staticmethod
    def binary_search(nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return l


if __name__ == '__main__':
    s = Solution()
    print(s.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
