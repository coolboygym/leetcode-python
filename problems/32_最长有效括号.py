class Solution2(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        return max(self.get_max(s, 0, len(s), 1, '('),
                   self.get_max(s, len(s) - 1, -1, -1, ')'))

    @staticmethod
    def get_max(chars, start, end, stride, char):
        curr_sum, result, curr_len, valid_len = 0, 0, 0, 0
        for i in range(start, end, stride):
            curr_sum += (1 if chars[i] == char else -1)
            curr_len += 1
            if curr_sum < 0:
                result = max(result, valid_len)
                curr_sum = 0
                curr_len = 0
                valid_len = 0
            elif curr_sum == 0:
                valid_len = curr_len
            else:
                pass

        return max(result, valid_len)


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: bool
        """
        from collections import deque

        stack = deque()
        for i, char in enumerate(s):
            if char == '(':
                stack.append((i, char))
            else:
                if len(stack) == 0:
                    stack.append((i, char))
                else:
                    last = stack.pop()
                    if last[1] != '(':
                        stack.append(last)
                        stack.append((i, char))

        if len(stack) == 0:
            return len(s)

        result, last_index = 0, -1
        for i, _ in stack:
            result = max(result, i - last_index - 1)
            last_index = i

        result = max(result, len(s) - last_index - 1)
        return result


if __name__ == '__main__':
    s = Solution()
    assert s.longestValidParentheses('(()') == 2
    assert s.longestValidParentheses(')()())') == 4
    assert s.longestValidParentheses('()(()') == 2
    assert s.longestValidParentheses('()(())') == 6
