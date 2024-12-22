from collections import defaultdict
class Solution:
    def longestEqualSubarray(self, nums: list[int], k: int) -> int:
        ### 对于数组里每个不同的值 做一次滑窗
        # 有个小技巧是 初始化时计算类似前缀和的值 可以简化后续的判断
        pos_list = defaultdict(list)
        # 初始化时对于每个x 保存在x之前和x不同的元素个数
        for i, x in enumerate(nums):
            pos_list[x].append(i - len(pos_list[x]))
        
        ans = 0 
        for pos in pos_list.values():
            # len(pos)即为当前value的数量
            # 如果总数量都已经小于ans 那当前value肯定不是最终那个值
            if len(pos) < ans:
                continue
            # 对当前value做一次滑窗
            l = 0
            for r, p in enumerate(pos):
                while p - pos[l] > k:
                    l += 1
                ans = max(r - l + 1, ans)
        return ans