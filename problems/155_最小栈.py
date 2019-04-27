class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        # 每次入栈时将当前最小值一起入栈 用空间换时间
        if len(self.stack) > 0:
            min_val = min(self.stack[-2], x)
        else:
            min_val = x
        self.stack.append(min_val)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) > 0:
            self.stack.pop()
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-2]
