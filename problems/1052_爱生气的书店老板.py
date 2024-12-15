class Solution:
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        n = len(customers)
        new_customers = [customers[i] * (grumpy[i] ^ 1) for i in range(minutes, n)]
        ans = total = sum(customers[:minutes]) + sum(new_customers)
        for i in range(minutes, n):
            if grumpy[i - minutes]:
                total -= customers[i - minutes]
            if grumpy[i]:
                total += customers[i]
            ans = max(ans, total)
        return ans