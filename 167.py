class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        i, j = 0, n - 1

        while True:
            result = numbers[i] + numbers[j]
            if result == target:
                return [i + 1, j + 1]
            elif result > target:
                j = j - 1
                while numbers[i] + numbers[j] > target:
                    j = j - 1
            else:
                i = i + 1
                while numbers[i] + numbers[j] < target:
                    i = i + 1


if __name__ == '__main__':
    s = Solution()
    assert s.twoSum(numbers=[2, 7, 11, 15], target=9) == [1, 2]
    assert s.twoSum(numbers=[1, 3, 5, 6, 7, 9, 11], target=13) == [4, 5]
