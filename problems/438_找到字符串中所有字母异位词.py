class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        ### 解题思路参照567_字符串的排列
        m = len(p)
        n = len(s)
        result = []
        if m > n:
            return result
        
        diff_cnt = [0] * 26     # 对于每个小写字母x 记录s中x的数量-p中x的数量
        total_diff = 0      # 记录s和p总共有多少个字母的数量不同
        base_ord = ord('a')

        for i in range(m):
            diff_cnt[ord(s[i]) - base_ord] += 1
            diff_cnt[ord(p[i]) - base_ord] -= 1
        
        for tmp in diff_cnt:
            if tmp != 0:
                total_diff += 1
        
        if total_diff == 0:     # 第一个窗口就满足 加入返回结果
            result.append(0)
        
        for i in range(m, n):
            x = ord(s[i]) - base_ord         # 入窗数据
            y = ord(s[i - m]) - base_ord     # 出窗数据
            if x == y:      # 新老数据一样 对窗口情况无影响 直接判断是否可以加入返回结果
                if total_diff == 0:
                    result.append(i - m + 1)
                continue

            if diff_cnt[x] == 0:    # 原本窗口和p里的x相等 现在新加入一个x 肯定就不等了
                total_diff += 1
            diff_cnt[x] += 1
            if diff_cnt[x] == 0:    # 原本窗口和p里的x不等 加入x后相等了 那么总的差值减1
                total_diff -= 1
            
            if diff_cnt[y] == 0:
                total_diff += 1
            diff_cnt[y] -= 1
            if diff_cnt[y] == 0:
                total_diff -= 1
            
            if total_diff == 0:
                result.append(i - m + 1)
        
        return result