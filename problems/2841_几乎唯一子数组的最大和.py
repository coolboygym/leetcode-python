from collections import Counter

### 标准滑窗三步走写法
class Solution0:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        n = len(nums)
        ans = total = 0
        diff_size = 0
        num_count = Counter()
        for i in range(n):
            if num_count[nums[i]] == 0:
                diff_size += 1
            num_count[nums[i]] += 1
            total += nums[i]
            
            if i < k - 1:
                continue
            
            if diff_size >= m:
                ans = max(ans, total)

            idx = i - k + 1
            num_count[nums[idx]] -= 1
            if num_count[nums[idx]] == 0:
                diff_size -= 1
            total -= nums[idx]

        return ans

### 先处理第一个窗口 减少后续冗余判断的写法
class Solution1:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        ans = 0
        n = len(nums)
        window = nums[:k]   # 处理第一个窗口
        num_count = Counter(window)
        diff_size = len(num_count)
        window_sum = sum(nums[:k])
        if len(num_count) >= m: # 这里要注意 ans和window_sum的初始化逻辑不一致
            ans = window_sum

        for i in range(k, n):
            # 老数据离开窗口
            out_idx = i - k
            num_count[nums[out_idx]] -= 1
            if num_count[nums[out_idx]] == 0:
                diff_size -= 1
            window_sum -= nums[out_idx]

            # 新数据进入窗口
            if num_count[nums[i]] == 0:
                diff_size += 1
            num_count[nums[i]] += 1
            window_sum += nums[i]
            
            # 更新答案
            if diff_size >= m:
                ans = max(ans, window_sum)

        return ans

### 思路同上一种 更简洁的写法
class Solution:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        ans = 0
        # 第一个窗口
        window = nums[:k]
        s = sum(window)
        cnt = Counter(window)
        if len(cnt) >= m:
            ans = s
        for in_, out in zip(nums[k:], nums):
            s += in_
            s -= out
            cnt[in_] += 1
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]
            if len(cnt) >= m:
                ans = max(ans, s)
        return ans


if __name__ == "__main__":
    solution = Solution()
    array = [1,1,1,3]
    result = solution.maxSum(array, 2, 2)
    print(result)
    assert result == 4