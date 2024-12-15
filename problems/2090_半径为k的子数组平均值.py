class Solution0:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        ans = [-1] * n
        size = k * 2 + 1    # 符合要求的子数组的大小
        if size > n:    # 子数组大小超过数组大小 说明没有满足条件的子数组
            return ans
        total = sum(nums[:size])    # 第一个符合要求的子数组求和
        ans[k] = total // size
        min_idx = -1
        curr_idx = k
        for i in range(size, n):
            curr_idx += 1
            min_idx += 1
            total = total - nums[min_idx] + nums[i]     # 窗口滑动 老数据离开 新数据加入
            ans[curr_idx] = total // size
        return ans
    

class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        ### 还是滑窗问题标准三步走
        n = len(nums)
        ans = [-1] * n  # 初始化返回结果
        total = 0
        s = k * 2
        size = k * 2 + 1    # 定义一些辅助变量 避免后面重复计算
        for i in range(n):
            # 1. 进入窗口
            total += nums[i]
            if i < s:   # 窗口大小不足2k+1
                continue
            
            # 2. 更新答案
            ans[i - k] = total // size
            
            # 3. 离开窗口
            total -= nums[i - s]
        return ans


if __name__ == "__main__":
    solution = Solution()
    array = [7,4,3,9,1,8,5,2,6]
    result = solution.getAverages(array, 3)
    print(result)