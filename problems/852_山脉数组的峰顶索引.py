class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        left = 1
        right = n - 2
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] > arr[mid+1]:   # 找第一个满足这个条件的下标
                ans = mid
                right = mid - 1                    
            else:
                left = mid + 1
        return ans