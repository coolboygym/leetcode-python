import heapq


class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        return [x[1] for x in heapq.nsmallest(K, [(p[0] ** 2 + p[1] ** 2, p) for p in points])]
