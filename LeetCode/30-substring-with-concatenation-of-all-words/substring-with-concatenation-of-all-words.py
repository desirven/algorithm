from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        answer = []
        window_size = len(words[0])
        word_cnt = Counter(words)

        for i in range(window_size):
            l, r = i, i
            s_cnt = Counter()

            while r+window_size <= len(s):
                word = s[r:r+window_size]
                r += window_size

                if word in word_cnt:
                    s_cnt[word] += 1
                
                    while s_cnt[word] > word_cnt[word]:
                        left_word = s[l:l+window_size]
                        s_cnt[left_word] -= 1
                        l += window_size

                    if r-l == len(words)*window_size:
                        answer.append(l)

                else:
                    s_cnt.clear()
                    l = r

        return answer
