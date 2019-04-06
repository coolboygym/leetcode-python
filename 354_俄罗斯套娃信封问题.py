class Solution1(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n <= 1:
            return n
        envelopes.sort(key=lambda x: x[0])
        dp = [1 for _ in range(n)]
        for i in range(1, n):
            for j in range(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        n = len(envelopes)
        if n <= 1:
            return n

        import functools

        """
        O(NlogN)的做法, 按照长度升序, 同长则宽度降序排列, 然后使用O(logN)
        的最长递增子序列解法(链接在评论中)来做即可. 排序后等于把在二维(长、宽)
        上的最长递增子序列问题转换成一维(宽)上的最长递增子序列的查找, 因为对于
        长度来说已经满足递增, 只需要在宽度上也递增即为递增序列, 同长时按宽度降
        序排列的原因是避免同长时宽度小的也被列入递增序列中, 例如[3,3], [3,4]
        如果宽度也按升序来排列, [3,3]和[3,4]会形成递增序列, 而实际上不行.
        """

        # 长度升序 同长则宽度降序排列
        def cmp(item1, item2):
            if item1[0] == item2[0]:
                if item2[1] >= item1[1]:
                    return 1
                else:
                    return -1
            if item1[0] > item2[0]:
                return 1
            else:
                return -1

        max_len = 0
        envelopes.sort(key=functools.cmp_to_key(cmp))
        dp = [-1 for _ in range(n)]
        for env in envelopes:
            low, high = 0, max_len
            # 循环退出的条件可以通过实际例子验证下
            while low < high:
                mid = low + (high - low) // 2
                # 必须找到比num[i]严格小的那个位置进行更新
                if env[1] > dp[mid]:
                    low = mid + 1
                else:
                    high = mid
            dp[low] = env[1]
            if low == max_len:
                max_len += 1
        return max_len
