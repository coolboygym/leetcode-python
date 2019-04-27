from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [x[1] for x in heapq.nlargest(k, [(v, k) for k, v in Counter(nums).items()])]


if __name__ == '__main__':
    s = Solution()
    assert s.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
