import collections


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # BFS 直接在迭代的时候进行判断 省去显式构建图的过程
        word_dict = set(wordList)
        if endWord not in word_dict:
            return 0

        word_level = dict()
        word_level[beginWord] = 1
        que = collections.deque()
        que.append(beginWord)
        all_chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        while len(que) > 0:
            word = que.popleft()
            for i, char in enumerate(word):
                for c in all_chars:
                    if c == char:
                        continue
                    temp_word = word[:i] + c + word[i + 1:]
                    if temp_word in word_dict:
                        word_level[temp_word] = word_level[word] + 1
                        word_dict.remove(temp_word)
                        if temp_word == endWord:
                            return word_level[temp_word]
                        que.append(temp_word)
        return 0


class Solution1(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # BFS优化版 两端搜索
        # 参考链接: https://leetcode-cn.com/problems/word-ladder/comments/21107
        word_dict = set(wordList)
        if endWord not in word_dict:
            return 0

        # 将beginWord也加入字典中 方便后面标记为已删除的操作
        word_dict.add(beginWord)
        begin_word_set = {beginWord}
        end_word_set = {endWord}
        all_chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        level = 1
        while len(begin_word_set) > 0:
            # 开始遍历新的一层
            level += 1
            temp_word_set = set()

            # 标记该层所有元素为已删除 避免同层节点之间相连
            for word in begin_word_set:
                word_dict.remove(word)

            for word in begin_word_set:
                for i, char in enumerate(word):
                    for c in all_chars:
                        if c == char:
                            continue
                        temp_word = word[:i] + c + word[i + 1:]
                        if temp_word in word_dict:
                            if temp_word in end_word_set:
                                return level
                            temp_word_set.add(temp_word)

            # 让begin_word_set始终作为更小的那个集合 减少运算量
            if len(temp_word_set) < len(end_word_set):
                begin_word_set = temp_word_set
            else:
                begin_word_set = end_word_set
                end_word_set = temp_word_set

        return 0
