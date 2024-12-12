from collections import defaultdict

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = defaultdict(int)
        for x in nums:
            cnt[x] += 1
        res = 0
        for val in cnt.values():
            res = res + val * (val-1) // 2  # 这里用到排列组合知识 在val中任取两个
        return res

if __name__ == '__main__':
    s = Solution()
    assert s.numIdenticalPairs([1,2,3,1,2,3]) == 3