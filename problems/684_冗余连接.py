class DisjointSet(object):
    def __init__(self):
        self.parent = {}

    def find(self, a):
        if a not in self.parent:
            self.parent[a] = a
            return a
        else:
            while a != self.parent[a]:
                a = self.parent[a]
            return a

    def union(self, a, b):
        root1 = self.find(a)
        root2 = self.find(b)
        if root1 != root2:
            self.parent[root2] = root1


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        ds = DisjointSet()
        for a, b in edges:
            if ds.find(a) == ds.find(b):
                return [a, b]
            else:
                ds.union(a, b)