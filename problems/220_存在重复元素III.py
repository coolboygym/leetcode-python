from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        ### 基本思路很直观 维护大小为indexDiff+1的窗口 每次判断新入窗数据与最接近的两个数的差值是否满足
        # 用到Python的第三方模块SortedList
        # 值得注意的是第一个窗口还没结束的时候可能已经得到答案了 对应倒数第三行len(window)
        n = len(nums)
        k = indexDiff + 1
        window = SortedList()
        for i in range(n):
            # 1.入
            window.add(nums[i])

            # 2.出
            if i >= k:
                window.remove(nums[i - k])

            # 3.判断并更新答案
            idx = window.bisect_left(nums[i])
            if idx > 0 and window[idx] - window[idx-1] <= valueDiff:
                return True
            if idx < len(window) - 1 and window[idx+1] - window[idx] <= valueDiff:
                return True

        return False