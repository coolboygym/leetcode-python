class Solution:
    def decrypt(self, code: list[int], k: int) -> list[int]:
        ### 滑动窗口问题 特别的点在于可以循环
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        size = abs(k)
        total = sum(code[:size-1])
        for i in range(size-1, n+size-1):
            # 新数据进入窗口
            total += code[i % n]

            # 计算结果 找到正确的位置
            # 小技巧 找个具体实例代入 便于计算与验证
            if k > 0:
                idx = (n + i - k) % n
            else:
                idx = (i + 1) % n
            ans[idx] = total

            # 老数据离开窗口
            total -= code[(i - size + 1) % n]
        return ans