class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        # 在二维矩阵上按照和递增顺序遍历 同时记录每个格子是否被访问过
        import heapq
        res = []
        h = []
        m, n = len(nums1), len(nums2)
        if m == 0 or n == 0 or k == 0:
            return res
        k = min(k, m * n)
        s = 1
        visited = set()
        heapq.heappush(h, (nums1[0] + nums2[0], 0, 0))
        visited.add((0, 0))
        while s <= k:
            item = heapq.heappop(h)
            i, j = item[1], item[2]
            res.append([nums1[i], nums2[j]])
            if i < m - 1 and (i + 1, j) not in visited:
                heapq.heappush(h, (nums1[i + 1] + nums2[j], i + 1, j))
                visited.add((i + 1, j))
            if j < n - 1 and (i, j + 1) not in visited:
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
                visited.add((i, j + 1))
            s += 1

        return res


if __name__ == '__main__':
    s = Solution()
    assert s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3) == [[1, 2], [1, 4], [1, 6]]
    assert s.kSmallestPairs([], [], 3) == []
    assert s.kSmallestPairs([1, 1, 2], [1, 2, 3], 10) == [[1, 1], [1, 1], [1, 2], [1, 2], [2, 1], [1, 3], [1, 3],
                                                          [2, 2], [2, 3]]
