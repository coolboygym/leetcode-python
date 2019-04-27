import heapq


class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._h_min = []
        self._h_max = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self._h_max) == len(self._h_min):
            if len(self._h_min) == 0 or num > self._h_min[0]:
                heapq.heappush(self._h_min, num)
            else:
                if num >= self._h_max[0] * -1:
                    heapq.heappush(self._h_min, num)
                else:
                    temp = heapq.heappop(self._h_max)
                    heapq.heappush(self._h_min, -1 * temp)
                    heapq.heappush(self._h_max, -1 * num)
        else:
            if num < self._h_min[0]:
                heapq.heappush(self._h_max, -1 * num)
            else:
                temp = heapq.heappop(self._h_min)
                heapq.heappush(self._h_min, num)
                heapq.heappush(self._h_max, -1 * temp)

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self._h_min) > len(self._h_max):
            return self._h_min[0]
        return (self._h_min[0] + self._h_max[0] * -1) / 2


if __name__ == '__main__':
    s = MedianFinder()
    s.addNum(1)
    s.addNum(2)
    print(s.findMedian())
    s.addNum(3)
    print(s.findMedian())

