# backtracking

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.result = []

        def dfs(start, l):
            if len(l) == 4 and start == len(s):
                self.result.append('.'.join(list(l)))
                return
            if start >= len(s) or start >= 12:
                return
            for m in range(1, 4):
                substr = s[start:start + m]
                if int(substr) > 255 or len(substr) > 1 and substr[0] == '0':
                    continue
                l.append(substr)
                dfs(start + m, l)
                l.pop()

        dfs(0, [])
        return self.result


if __name__ == '__main__':
    s = Solution()
    print(s.restoreIpAddresses("010010"))
