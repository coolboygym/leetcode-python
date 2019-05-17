class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s = sum(A)
        if s % 3 != 0:
            return False
        target = s // 3
        curr_sum = 0
        for i in range(len(A)):
            curr_sum += A[i]
            if curr_sum == target:
                curr_sum = 0
        return curr_sum == 0
