class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y, z = 0, x
        while x:
            y *= 10
            y += (x % 10)
            x //= 10
        if z == y:
            return True
        return False


if __name__ == '__main__':
    s = Solution()
    assert s.isPalindrome(919) is True
