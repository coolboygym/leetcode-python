class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 贪心法 reach表示跳跃step步之后最远能够到达的距离
        if len(nums) < 2:
            return 0
        reach, step, next_reach, n = 0, 0, 0, len(nums)
        for i in range(n):
            next_reach = max(next_reach, i+nums[i])
            if next_reach >= n - 1:
                return step + 1
            if i == reach:
                step += 1
                reach = next_reach
