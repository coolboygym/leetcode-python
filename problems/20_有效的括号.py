class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import deque

        left_part = '({['
        r_l_map = {
            '(': ')',
            '{': '}',
            '[': ']',
            '.': '.'
        }

        q = deque()
        q.append('.')  # 用于处理空字符串和只有右括号的情况
        for x in s:
            if x in left_part:
                q.append(x)
            else:
                y = q.pop()
                if x != r_l_map[y]:
                    return False

        return len(q) == 1


if __name__ == '__main__':
    s = Solution()
    assert s.isValid("[") is False
