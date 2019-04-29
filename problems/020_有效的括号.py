class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 使用栈进行符号匹配 碰到左括号入栈 碰到右括号出栈并检查
        left_part = '({['
        left_right_map = {
            '(': ')',
            '{': '}',
            '[': ']',
            '.': '.'
        }

        # 预先放入一个标识符 用于处理空字符串和只包含右括号的情况
        q = ['.']
        for x in s:
            if x in left_part:
                q.append(x)
            else:
                y = q.pop()
                if x != left_right_map[y]:
                    return False

        return len(q) == 1


if __name__ == '__main__':
    s = Solution()
    assert s.isValid("[") is False
