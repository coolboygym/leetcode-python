class Solution(object):
    def countGoodTriplets(self, arr, a, b, c):
        """
        :type arr: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: int
        """
        size = len(arr)
        if size < 3:
            return 0
        res = 0
        for i in range(size-2):
            for j in range(i+1, size-1):
                if abs(arr[i]-arr[j]) > a:  # 提前判断减少后续不必要的循环
                    continue
                for k in range(j+1, size):
                    if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                        res += 1
        return res


if __name__ == '__main__':
    s = Solution()
    assert s.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3) == 4