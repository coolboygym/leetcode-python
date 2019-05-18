import collections


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        # 把同岁的人放在一起考虑
        age = collections.Counter(ages)
        res = 0
        for a in age:
            for b in age:
                if b <= 0.5 * a + 7 or b > a:
                    continue
                res += age[a] * (age[b] - (a == b))
        return res
