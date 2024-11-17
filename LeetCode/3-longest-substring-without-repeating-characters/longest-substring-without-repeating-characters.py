class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l,r = 0,0
        answer = 0
        while r < len(s):
            if s[r] not in charSet:
                charSet.add(s[r])
                r += 1
            else:
                while s[r] in charSet and l<=r:
                    answer = max(answer, r-l)
                    charSet.remove(s[l])
                    l += 1
        answer = max(answer, r-l)
        return answer