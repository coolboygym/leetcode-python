class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        arr = sorted(list(range(lo, hi+1)), key=self.get_weight)
        return arr[k - 1]
    
    def get_weight(self, x):
        weight = 0
        while x != 1:
            if x % 2 == 0:
                x //= 2
            else:
                x = x * 3 + 1
            weight += 1
        return weight