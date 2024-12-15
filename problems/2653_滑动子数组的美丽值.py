class Solution:
    def getSubarrayBeauty(self, nums: list[int], k: int, x: int) -> list[int]:
        cnt = [0] * 101     # 记录窗口内每个数的数量
        neg_cnt = 0     # 记录窗口内负数的数量 简化部分判断
        for num in nums[:k - 1]:  # 先往窗口内添加 k-1 个数
            cnt[num] += 1
            neg_cnt += int(num < 0)
        ans = [0] * (len(nums) - k + 1)
        for i, (in_, out) in enumerate(zip(nums[k - 1:], nums)):
            cnt[in_] += 1  # 进入窗口（保证窗口有恰好 k 个数）
            neg_cnt += int(in_ < 0)
            if neg_cnt < x: # 负数个数不到x 第x小的数肯定非负数 直接跳过后续判断
                cnt[out] -= 1
                neg_cnt -= int(out < 0)
                continue

            left = x
            for j in range(-50, 0):  # 暴力枚举负数范围 [-50,-1]
                left -= cnt[j]
                if left <= 0:  # 找到美丽值
                    ans[i] = j
                    break
            
            cnt[out] -= 1  # 离开窗口
            neg_cnt -= int(out < 0)

        return ans
    

if __name__ == "__main__":
    pass