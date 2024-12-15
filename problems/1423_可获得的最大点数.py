### 比较直观的解法
class Solution0:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        ans = total = sum(cardPoints[:k])
        if k == n:
            return ans
        for i in range(k):
            total -= cardPoints[k - 1 - i]
            total += cardPoints[n - 1 - i]
            ans = max(ans, total)
        return ans

### 反过来想 相当于有n-k个连续元素不在最后的结果里 求n-k大小的窗口内最小值即可
class Solution:
    def maxScore(self, cardPoints: list[int], k: int) -> int:
        n = len(cardPoints)
        total_sum = sum(cardPoints)
        if k == n:
            return total_sum
        new_k = n - k
        min_sum = total = sum(cardPoints[:new_k])
        for i in range(new_k, n):
            total -= cardPoints[i - new_k]
            total += cardPoints[i]
            min_sum = min(min_sum, total)
        return total_sum - min_sum


if __name__ == "__main__":
    solution = Solution()
    array = [1,1000,1]
    result = solution.maxScore(array, 1)
    print(result)
    assert result == 1
    array = [1,79,80,1,1,1,200,1]
    result = solution.maxScore(array, 3)
    assert result == 202

