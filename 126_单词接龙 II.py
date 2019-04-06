class Solution1(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        word_dict = set(wordList)
        if endWord not in word_dict:
            return []

        # 将beginWord也加入字典中 方便后面标记为已删除的操作
        word_dict.add(beginWord)
        res = []
        flag, next_word_map = self.bfs(beginWord, endWord, word_dict)
        if not flag:
            self.dfs(beginWord, endWord, next_word_map, [beginWord], res)
        return res

    def bfs(self, begin_word, target, word_dict):
        begin_word_set = {begin_word}
        flag = True
        next_word_map = dict()
        all_chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        while len(begin_word_set) > 0 and flag:
            # 开始遍历新的一层
            temp_word_set = set()
            for word in begin_word_set:
                # 标记该层所有元素为已删除 避免同层节点之间相连
                word_dict.remove(word)

            for word in begin_word_set:
                next_word_map[word] = set()
                for i, char in enumerate(word):
                    for c in all_chars:
                        if c == char:
                            continue
                        temp_word = word[:i] + c + word[i + 1:]
                        if temp_word in word_dict:
                            if temp_word == target:
                                # 设置标志位 表示这一层结束后就可以返回结果了
                                flag = False
                            temp_word_set.add(temp_word)
                            next_word_map[word].add(temp_word)
            begin_word_set = temp_word_set
        return flag, next_word_map

    def dfs(self, curr_word, target, next_word_map, path, result):
        if curr_word == target:
            result.append(list(path))
            return

        # 和target处于同一层的单词在next_word_map里还没有对应的项
        if curr_word in next_word_map:
            for next_word in next_word_map[curr_word]:
                path.append(next_word)
                self.dfs(next_word, target, next_word_map, path, result)
                path.pop()


class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        # 评论区大佬解法 优化的BFS 双端搜索
        from collections import defaultdict
        if endWord not in wordList:
            return []
        forward, backward, wordList, dic = {beginWord}, {endWord}, set(wordList), defaultdict(set)
        flag, letters, length = True, set('qwertyuioplkjhgfdsazxcvbnm'), len(endWord)
        while forward:
            if len(forward) > len(backward):
                forward, backward, flag = backward, forward, not flag
            cur = set()
            wordList -= forward
            for word in forward:
                for idx in range(length):
                    x, y = word[:idx], word[idx + 1:]
                    for letter in letters:
                        temp = x + letter + y
                        if temp in wordList:
                            cur.add(temp)
                            if flag:
                                dic[temp].add(word)
                            else:
                                dic[word].add(temp)
            if cur & backward:
                res = [[endWord]]
                # 生成最终结果 每次迭代添加一层 上次迭代的结果作为下次迭代的起点 每次走一步的做法！！！
                while res[0][0] != beginWord:
                    res = [[x] + y for y in res for x in dic[y[0]]]
                return res
            forward = cur
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.findLadders('hit', 'cog', ["hot", "dot", "dog", "lot", "log", "cog"]))
    print(s.findLadders('a', 'c', ['a', 'b', 'c']))
