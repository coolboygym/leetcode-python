class Solution:
    def minFlips(self, s: str) -> int:
        ### 第一个条件实际就是循环数组 用滑动窗口 窗口大小为数组长度
        # 实际上最终字符串只能是01重复 或者10重复
        # 最重要的逻辑是 如果将字符串s改为按照01重复需要m次 那么改为10重复则需要n-m次
        n = len(s)
        ans = cnt = 0
        target_str = '01'

        # 先遍历一遍原始字符串 计算基准值 相当于第一次滑窗
        # cnt是把字符串s改为01重复序列的次数
        for i in range(n):
            cnt += (s[i] != target_str[i % 2])
        ans = min(cnt, n - cnt)

        # 开始滑窗
        for i in range(n):
            cnt -= (s[i] != target_str[i % 2])  # 旧数据离开窗口
            cnt += (s[i] != target_str[(i + n) % 2])    # 新数据进入窗口
            ans = min(ans, cnt, n - cnt)    # 更新答案
        
        return ans