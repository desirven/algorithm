class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        answer = 0
        while r < len(s):
            if s[r] not in s[l:r]:
                r += 1
            else:
                while s[r] in s[l:r] and l<=r:
                    answer = max(answer, r-l)
                    l += 1
        answer = max(answer, r-l)
        return answer