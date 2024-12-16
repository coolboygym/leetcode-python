from collections import Counter
class Solution0:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 通过两个counter的比较来判断是否正确 时间复杂度O(m*n)
        m = len(s1)
        n = len(s2)
        counter_1 = Counter(s1)
        left = 0
        right = m - 1
        counter_2 = Counter(s2[:right])   # 初始化第一个窗口
        while right < n:
            # 1. 入
            counter_2[s2[right]] += 1

            # 2. 更新
            if counter_1 == counter_2:
                return True

            # 3. 出
            counter_2[s2[left]] -= 1
            if counter_2[s2[left]] == 0:
                del counter_2[s2[left]]
            
            left += 1
            right += 1
        
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # 整体逻辑同上 优化两个counter做相等比较的逻辑 动态比较每次字符出入 减小时间复杂度
        # 参考力扣官方解答
        m = len(s1)
        n = len(s2)
        if m > n:
            return False
        
        diff_cnt = [0] * 26     # 对于每个小写字母x 记录s2中x的数量-s1中x的数量
        total_diff = 0      # 记录s1和s2总共有多少个字母的数量不同
        base_ord = ord('a')

        for i in range(m):
            diff_cnt[ord(s2[i]) - base_ord] += 1
            diff_cnt[ord(s1[i]) - base_ord] -= 1
        
        for tmp in diff_cnt:
            if tmp != 0:
                total_diff += 1
        
        if total_diff == 0:     # 第一个窗口就满足 直接返回
            return True
        
        for i in range(m, n):
            x = ord(s2[i]) - base_ord         # 入窗数据
            y = ord(s2[i - m]) - base_ord     # 出窗数据
            if x == y:      # 新老数据一样 对窗口情况无影响 直接跳过
                continue
            if diff_cnt[x] == 0:    # 原本窗口和s1里的x相等 现在新加入一个x 肯定就不等了
                total_diff += 1
            diff_cnt[x] += 1
            if diff_cnt[x] == 0:    # 原本窗口和s1里的x不等 加入x后相等了 那么总的差值减1
                total_diff -= 1
            
            if diff_cnt[y] == 0:
                total_diff += 1
            diff_cnt[y] -= 1
            if diff_cnt[y] == 0:
                total_diff -= 1
            
            if total_diff == 0:
                return True
        
        return False