from collections import defaultdict

class FreqStack(object):

    def __init__(self):
        self.max_freq = 0
        self.freq = defaultdict(list)
        self.occurrence = {}

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.occurrence[x] = self.occurrence.get(x,0)+1
        if self.occurrence[x] >= self.max_freq:
            self.max_freq = self.occurrence[x]
        self.freq[self.occurrence[x]].append(x)

    def pop(self):
        """
        :rtype: int
        """
        popped = self.freq[self.max_freq].pop(-1)
        if not self.freq[self.max_freq]:
            self.max_freq -= 1
        self.occurrence[popped] -= 1
        return popped


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()