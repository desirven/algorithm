class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s)==0:
            return True
        idx_s = 0
        for c in t:
            if c == s[idx_s]:
                idx_s += 1
            if idx_s >= len(s):
                return True
        return False