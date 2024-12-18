from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        one_word = len(words[0])
        word_num = len(words)
        n = len(s)
        if n < one_word * word_num:
            return []
        words = Counter(words)
        res = []
        for i in range(0, one_word):    # 遍历每一种可能的开头
            cur_cnt = 0
            left = i
            right = i
            cur_Counter = Counter()
            while right + one_word <= n:
                w = s[right:right + one_word]
                right += one_word
                if w not in words:  # 在s中碰到一个不在words里的字符串 可以从它下一个word重新开始
                    left = right
                    cur_Counter.clear()
                    cur_cnt = 0
                else:
                    cur_Counter[w] += 1
                    cur_cnt += 1
                    while cur_Counter[w] > words[w]:
                        left_w = s[left:left+one_word]
                        left += one_word
                        cur_Counter[left_w] -= 1
                        cur_cnt -= 1
                    if cur_cnt == word_num :
                        res.append(left)
        return res
