# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count, max_count = 0, 0
        for idx in range(len(s)):
            if s[idx] in s[idx-count:idx]:
                max_count = max(count, max_count)
                count -= 1
            else:
                count += 1
        max_count = max(count, max_count)
        return max_count
