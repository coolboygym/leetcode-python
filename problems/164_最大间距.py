class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 桶排序
        # 参考：https://blog.csdn.net/zxzxzx0119/article/details/82889998
        # 设置n+1个桶是为了保证间距最大的两个数被分到不同的桶中
        # 因为最大间距 x >= (max_val - min_val) / (n-1)
        # 而使用n+1个桶每个桶中数的差值最大为 (max_val - min_val) / n 因此一个桶不可能同时存放间距最大的两个数
        if len(nums) < 2:
            return 0
        min_val, max_val, n = float('inf'), float('-inf'), len(nums)
        for i in range(n):
            if nums[i] < min_val:
                min_val = nums[i]
            if nums[i] > max_val:
                max_val = nums[i]

        if min_val == max_val:
            return 0

        mins = [0] * (n + 1)
        maxs = [0] * (n + 1)
        has_num = [False] * (n + 1)

        for num in nums:
            index = int((num - min_val) * n / (max_val - min_val))
            mins[index] = num if not has_num[index] else min(mins[index], num)
            maxs[index] = num if not has_num[index] else max(maxs[index], num)
            has_num[index] = True

        max_len = 0
        m = maxs[0]
        for i in range(1, n + 1):
            if has_num[i]:
                curr_len = mins[i] - m
                if curr_len > max_len:
                    max_len = curr_len
                m = maxs[i]

        return max_len
