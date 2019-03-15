class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        if len(height) < 2:
            return 0

        max_height = max(height)
        water = 0
        length = len(height)

        for i in range(max_height):
            index_arr = []
            for j in range(length):
                if height[j] > i:
                    index_arr.append(j)

            water += (index_arr[-1] - index_arr[0] - len(index_arr) + 1)

        return water


if __name__ == '__main__':
    s = Solution()
    h = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    res = s.trap(h)
    print(res)
