from collections import Counter
import heapq


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # c = Counter(nums)
        # items = [(v, k) for k, v in Counter(nums).items()]
        return [x[1] for x in heapq.nlargest(k, [(v, k) for k, v in Counter(nums).items()])]


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))
