class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 先排序 后朴素递归
        candidates.sort()
        result = []
        n = len(candidates)

        # 对数组元素进行遍历 依次处理每个元素 避免产生重复的组合
        for i in range(n):
            c = candidates[i]
            if target % c == 0:
                result.append([c] * (target // c))

            # 这里k的遍历终点是target // c - 1 而非target // c
            # 由于数组已排序 当k等于target // c 时余下的target肯定比之后所有数都更小 无需尝试
            for k in range(1, target // c):
                temp = [c] * (target // c - k)
                res = self.combinationSum(candidates[i + 1:], target % c + k * c)
                if res:
                    for r in res:
                        result.append(temp + r)

        return result
