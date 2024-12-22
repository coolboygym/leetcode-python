from bisect import bisect_left

class Solution:
    def maxTotalFruits(self, fruits: list[list[int]], startPos: int, k: int) -> int:
        ### 重点是对每一个有水果的坐标做滑窗 而不是对每一个坐标滑窗
        # 要么先左走再右走 要么先右走再左走 能摘到的水果是最多的
        left = bisect_left(fruits, [startPos - k])  # 向左最远能到 fruits[left][0]
        right = bisect_left(fruits, [startPos + 1])  # startPos 右边最近水果（因为下面求的是左闭右开区间）
        ans = s = sum(c for _, c in fruits[left:right])  # 从 fruits[left][0] 到 startPos 的水果数
        while right < len(fruits) and fruits[right][0] <= startPos + k:
            s += fruits[right][1]  # 枚举最右位置为 fruits[right][0]
            while fruits[right][0] * 2 - fruits[left][0] - startPos > k and \
                  fruits[right][0] - fruits[left][0] * 2 + startPos > k:
                s -= fruits[left][1]  # fruits[left][0] 无法到达
                left += 1
            ans = max(ans, s)  # 更新答案最大值
            right += 1  # 继续枚举下一个最右位置
        return ans