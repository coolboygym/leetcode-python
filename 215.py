class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq

        n = len(nums)
        if k > n // 2:
            return heapq.nsmallest(n + 1 - k, nums)[-1]
        else:
            return heapq.nlargest(k, nums)[-1]
