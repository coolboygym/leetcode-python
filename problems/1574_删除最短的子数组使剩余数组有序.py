class Solution0:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        ### 删除子数组后 最终结果一定是最前面一个非递减子数组+最后面一个非递减子数组
        # 先找到符合要求的左端点 然后枚举右端点 移动左端点
        n = len(arr)
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
        if left == n - 1:   # arr本身符合要求
            return 0
        
        ans = n - left - 1
        right = n - 1
        while right == n - 1 or arr[right] <= arr[right+1]:
            while left >= 0 and arr[left] > arr[right]:
                left -= 1
             # 此时 arr[left] <= arr[right]，删除 arr[left+1:right-1]
            ans = min(ans, right - left - 1)
            right -= 1
        return ans


class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        # 先找到符合要求的右端点 然后枚举右端点 移动左端点
        n = len(arr)
        right = n - 1
        while right and arr[right - 1] <= arr[right]:
            right -= 1
        if right == 0:  # arr 已经是非递减数组
            return 0
        # 此时 arr[right-1] > arr[right]
        ans = right  # 删除 arr[:right]
        left = 0
        while True:  # 枚举 right
            while right == n or arr[left] <= arr[right]:
                ans = min(ans, right - left - 1)  # 删除 arr[left+1:right]
                if arr[left] > arr[left + 1]:
                    return ans
                left += 1
            right += 1