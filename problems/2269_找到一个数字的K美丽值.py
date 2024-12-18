class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ### 纯数学计算 不断取最低的 k 位数字，判断后，去掉末尾数字，不断循环直到不足 k 位数字
        ans = 0
        t = num
        m = 10**k
        mm = m // 10
        while t >= mm:  # 当前剩余的数大于K位
            w = t % m   # 得到当前最低的K位数
            if w and num % w == 0:  # 不为0且能被num整除 当前数满足题意
                ans += 1
            t //= 10    # 去掉最低位
        return ans