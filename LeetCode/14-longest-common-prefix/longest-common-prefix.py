class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 0:
            return prefix
        for i in range(len(strs[0])):
            for str in strs[1:]:
                if i == len(str) or str[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix