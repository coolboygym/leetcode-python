class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 拓扑排序 判断有向图中是否存在环
        if numCourses == 0 or len(prerequisites) == 0:
            return True

        import collections
        in_degrees = [0 for _ in range(numCourses)]
        node_childes = [[] for _ in range(numCourses)]

        for child, parent in prerequisites:
            in_degrees[child] += 1
            node_childes[parent].append(child)

        # 入度为0节点入队
        que = collections.deque()
        for i in range(numCourses):
            if in_degrees[i] == 0:
                que.append(i)

        counter = 0
        while len(que) > 0:
            parent = que.popleft()
            counter += 1

            # 后继节点入度减1
            for child in node_childes[parent]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    que.append(child)

        return counter == numCourses


if __name__ == '__main__':
    s = Solution()
    assert s.canFinish(2, [[1, 0]]) is True
