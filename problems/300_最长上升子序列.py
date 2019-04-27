class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 动态规划的核心：在求解规模为n的问题时 你已经知道了规模小于n的所有问题的答案
        # 动态规划的思路：将 dp 数组定义为：以 nums[i] 结尾的最长上升子序列的长度
        # 那么题目要求的，就是这个 dp 数组中的最大者
        # 以数组  [10, 9, 2, 5, 3, 7, 101, 18] 为例：
        # dp 的值： 1  1  1  2  2  3  4  4
        n = len(nums)
        if n <= 1:
            return n
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        本解法的核心在于：如何更好地定义dp数组
        dp[i]: 所有长度为i + 1
        的递增子序列中, 最小的那个序列尾数.
        由定义知dp数组必然是一个递增数组, 可以用
        maxL
        来表示最长递增子序列的长度.
        对数组进行迭代, 依次判断每个数num将其插入dp数组相应的位置:
        1.
        num > dp[maxL], 表示num比所有已知递增序列的尾数都大, 将num添加入dp
        数组尾部, 并将最长递增序列长度maxL加1
        2.
        dp[i - 1] < num <= dp[i], 只更新相应的dp[i]
        """
        n = len(nums)
        if n <= 1:
            return n
        max_len = 0
        dp = [-1 for _ in range(n)]
        for num in nums:
            low, high = 0, max_len
            # 循环退出的条件可以通过实际例子验证下
            while low < high:
                mid = low + (high - low) // 2
                # 必须找到比num[i]严格小的那个位置进行更新
                if num > dp[mid]:
                    low = mid + 1
                else:
                    high = mid
            dp[low] = num
            if low == max_len:
                max_len += 1
        return max_len
