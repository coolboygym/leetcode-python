class Solution1(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 一次遍历 最小堆+计数器
        import heapq
        from collections import defaultdict

        if not nums:
            return []

        nums = [-1 * x for x in nums]
        counter = defaultdict(int)

        windows = nums[:k]
        res = []
        heapq.heapify(windows)
        res.append(-1 * windows[0])
        counter[nums[0]] += 1
        for i in range(len(nums) - k):
            heapq.heappush(windows, nums[i + k])
            min_num = windows[0]
            while counter[min_num] > 0:
                counter[min_num] -= 1
                heapq.heappop(windows)
                min_num = windows[0]
            res.append(-1 * min_num)
            counter[nums[i + 1]] += 1

        return res


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque

        res = []

        q = deque()

        for idx, v in enumerate(nums):

            # 检查如果左边界超出窗口就弹出队列头

            if len(q) > 0 and q[0] <= idx - k:
                q.popleft()

            # 循环检查队尾是否大于当前元素

            while len(q) > 0 and nums[q[-1]] < v:
                q.pop()

            q.append(idx)

            if idx >= k - 1:
                res.append(nums[q[0]])

        return res


if __name__ == '__main__':
    s = Solution()
    # print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(s.maxSlidingWindow([9, 10, 9, -7, -4, -8, 2, -6], 5))
    print(s.maxSlidingWindow(
        [-95, 92, -85, 59, -59, -14, 88, -39, 2, 92, 94, 79, 78, -58, 37, 48, 63, -91, 91, 74, -28, 39, 90, -9, -72,
         -88, -72, 93, 38, 14, -83, -2, 21, 4, -75, -65, 3, 63, 100, 59, -48, 43, 35, -49, 48, -36, -64, -13, -7, -29,
         87, 34, 56, -39, -5, -27, -28, 10, -57, 100, -43, -98, 19, -59, 78, -28, -91, 67, 41, -64, 76, 5, -58, -89, 83,
         26, -7, -82, -32, -76, 86, 52, -6, 84, 20, 51, -86, 26, 46, 35, -23, 30, -51, 54, 19, 30, 27, 80, 45, 22],
        10))
