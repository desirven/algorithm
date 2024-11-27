class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        replace_map = {}
        for i in range(len(pattern)):
            if pattern[i] not in replace_map:
                if s[i] in replace_map.values():
                    return False
                replace_map[pattern[i]] = s[i]
            elif replace_map[pattern[i]] == s[i]:
                continue
            else:
                return False
        return True