from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        elif s == t:
            return s
        
        cnt_t = Counter(t)
        filtered_s = [(i, c) for i, c in enumerate(s) if c in cnt_t]

        l, r = 0, 0
        cnt_w = Counter()

        answer = float("inf"), None, None

        for r in range(len(filtered_s)):
            c = filtered_s[r][1]
            cnt_w[c] += 1

            if all(cnt_w[char] >= count for char, count in cnt_t.items()):
                while l <= r:
                    c = filtered_s[l][1]

                    end = filtered_s[r][0]
                    start = filtered_s[l][0]
                    if end-start+1 < answer[0]:
                        answer = (end-start+1, start, end)
                    
                    cnt_w[c] -= 1
                    l += 1
                    if cnt_w[c] < cnt_t[c]:
                        break

        return "" if answer[0] == float("inf") else s[answer[1] : answer[2] + 1]