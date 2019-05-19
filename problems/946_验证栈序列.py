class Solution(object):
    def validateStackSequences(self, pushed, popped):
        """
        :type pushed: List[int]
        :type popped: List[int]
        :rtype: bool
        """
        stack = []
        while pushed or stack:
            if not stack:
                item = pushed.pop(0)
                stack.append(item)
            elif pushed and stack[-1] != popped[0]:
                item = pushed.pop(0)
                stack.append(item)
            elif stack and stack[-1] == popped[0]:
                stack.pop(-1)
                popped.pop(0)
            else:
                return False
        return len(stack) == 0