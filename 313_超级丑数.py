class Solution:
    def nthSuperUglyNumber(self, n, primes):

        nums = [None for x in range(n)]
        nums[0] = 1
        k = len(primes)

        carry_list = [0 for _ in range(k)]
        number_min = [0 for _ in range(k)]

        for i in range(1, n):
            for j in range(k):
                number_min[j] = nums[carry_list[j]] * primes[j]
            nums[i] = min(number_min)
            for j in range(k):
                if nums[i] == number_min[j]:
                    carry_list[j] += 1
        return nums[n - 1]
