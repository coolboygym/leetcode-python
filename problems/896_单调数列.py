class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # 维护一个状态变量作为开关
        nPreStatus = 0
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                if nPreStatus == -1:
                    return False
                else:
                    nPreStatus = 1
            elif A[i] < A[i + 1]:
                if nPreStatus == 1:
                    return False
                else:
                    nPreStatus = -1
        return True
