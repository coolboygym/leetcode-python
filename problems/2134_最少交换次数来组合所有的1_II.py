class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        ### 重点在于如何转化为滑动窗口问题
        # 总共有K个1 问题变成求大小为K的窗口内1最多出现的次数 最后返回结果减一下即可
        # 注意循环数组的下标
        total_cnt = sum(nums)
        if total_cnt <= 1:
            return 0
        n = len(nums)
        max_cnt = 0
        curr_cnt = sum(nums[:total_cnt - 1])
        for i in range(n):
            # 1.进入窗口
            idx = (i + total_cnt - 1) % n
            curr_cnt += nums[idx]

            # 2.更新答案
            max_cnt = max(max_cnt, curr_cnt)
            
            # 3.离开窗口
            curr_cnt -= nums[i]
        return total_cnt - max_cnt