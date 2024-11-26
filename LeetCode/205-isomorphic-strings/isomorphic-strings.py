class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        replace_map = {}
        for i in range(len(s)):
            if s[i] not in replace_map:
                if t[i] in replace_map.values():
                    return False
                replace_map[s[i]] = t[i]
            elif replace_map[s[i]] == t[i]:
                continue
            else:
                return False
        return True