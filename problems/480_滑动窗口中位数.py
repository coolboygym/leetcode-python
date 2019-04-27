class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """
        if not nums:
            return []

        res = list()
        windows = list()
        for i in range(k):
            pos = self.binary_search(windows, i, nums[i])
            windows.insert(pos, nums[i])
        res.append((windows[k >> 1] + windows[(k - 1) >> 1]) / 2)

        for idx in range(k, len(nums)):
            pos = self.binary_search(windows, k, nums[idx - k])
            windows.pop(pos)
            pos = self.binary_search(windows, k - 1, nums[idx])
            windows.insert(pos, nums[idx])
            res.append((windows[k >> 1] + windows[(k - 1) >> 1]) / 2)

        return res

    @staticmethod
    def binary_search(nums, size, target):
        l = 0
        r = size - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return l


class HashHeap:
    def __init__(self, desc=False):
        self.hash = dict()
        self.heap = [-1]  # 根节点保存在下标为1的位置
        self.desc = desc
        self.size = 0

    def push(self, item):
        self.heap.append(item)
        self.size += 1
        self.hash[item] = self.size
        self._sift_up(self.size)

    def pop(self):
        item = self.heap[1]
        self.remove(item)
        return item

    def top(self):
        return self.heap[1]

    def remove(self, item):
        # in case of heap is empty or bad remove request
        if item not in self.hash:
            return

        index = self.hash[item]
        self._swap(index, self.size)

        del self.hash[item]
        self.heap.pop()
        self.size -= 1

        # in case of the removed item is the last item
        if index < self.size:
            self._sift_up(index)
            self._sift_down(index)

    def _smaller(self, left, right):
        return right < left if self.desc else left < right

    def _sift_up(self, index):
        while index > 1:
            parent = index // 2
            if self._smaller(self.heap[parent], self.heap[index]):
                break
            self._swap(parent, index)
            index = parent

    def _sift_down(self, index):
        while index * 2 <= self.size:
            child = index * 2
            if child != self.size and self._smaller(self.heap[child + 1], self.heap[child]):
                child = child + 1

            if self._smaller(self.heap[child], self.heap[index]):
                self._swap(index, child)
            else:
                break

            index = child

    def _swap(self, i, j):
        elem1 = self.heap[i]
        elem2 = self.heap[j]
        self.heap[i] = elem2
        self.heap[j] = elem1
        self.hash[elem1] = j
        self.hash[elem2] = i


class Solution1:
    def __init__(self):
        self.max_heap = HashHeap(desc=True)
        self.min_heap = HashHeap()
        self.window_size_odd = True

    def medianSlidingWindow(self, nums, k):
        if not nums or len(nums) < k:
            return []

        self.window_size_odd = (k % 2 == 1)
        for i in range(0, k - 1):
            self.add((nums[i], i))

        medians = []
        for i in range(k - 1, len(nums)):
            self.add((nums[i], i))
            medians.append(self.median)
            self.remove((nums[i - k + 1], i - k + 1))

        return medians

    def add(self, item):
        if self.max_heap.size > self.min_heap.size:
            self.min_heap.push(item)
        else:
            self.max_heap.push(item)

        if self.max_heap.size == 0 or self.min_heap.size == 0:
            return

        if self.max_heap.top() > self.min_heap.top():
            item1 = self.min_heap.pop()
            item2 = self.max_heap.pop()
            self.max_heap.push(item1)
            self.min_heap.push(item2)

    def remove(self, item):
        if item > self.max_heap.top():
            self.min_heap.remove(item)
        else:
            self.max_heap.remove(item)

    @property
    def median(self):
        if self.window_size_odd:
            return self.max_heap.top()[0] * 1.0
        else:
            return (self.max_heap.top()[0] + self.min_heap.top()[0]) / 2


if __name__ == '__main__':
    s = Solution()
    assert s.medianSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    s = Solution()
    assert s.medianSlidingWindow([1, 4, 2, 3], 4) == [2.5]
    s = Solution()
    assert s.medianSlidingWindow([1], 1) == [1.0]
    s = Solution()
    assert s.medianSlidingWindow([5, 5, 8, 1, 4, 7, 1, 3, 8, 4], 8) == [4.5, 4.5, 4.0]
