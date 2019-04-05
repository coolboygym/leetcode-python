class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        total = m + n
        if total % 2:
            return self.findKth(nums1, m, nums2, n, total // 2 + 1)
        else:
            return (self.findKth(nums1, m, nums2, n, total // 2)
                    + self.findKth(nums1, m, nums2, n, total // 2 + 1)) / 2

    def findKth(self, nums1, m, nums2, n, k):
        # 保证A数组的大小不大于B数组 简化后面的逻辑判断
        if m > n:
            return self.findKth(nums2, n, nums1, m, k)

        # 数组A为空 直接返回数组B第k小的数
        if m == 0:
            return nums2[k - 1]

        # k等于1时终止递归 防止数组A下标越界
        if k == 1:
            return min(nums1[0], nums2[0])

        pa = min(k // 2, m)  # 取min是防止访问数组A时下标越界
        pb = k - pa

        if nums1[pa - 1] < nums2[pb - 1]:
            return self.findKth(nums1[pa:], m - pa, nums2, n, k - pa)
        elif nums1[pa - 1] > nums2[pb - 1]:
            return self.findKth(nums1, m, nums2[pb:], n - pb, k - pb)
        else:
            return nums1[pa - 1]


if __name__ == '__main__':
    s = Solution()
    print(s.findKth([1, 3, 17], 3, [2, 9, 11, 14], 4, 5))
    print(s.findMedianSortedArrays([1, 3], [2, 4]))
