class Solution:
    def convert(self, s: str, numRows: int) -> str:
        summarized_s = [[] for _ in range(numRows)]
        pattern = list(range(numRows)) + list(range(numRows-2, 0, -1))
        for idx in range(len(s)):
            summarized_s[pattern[idx%len(pattern)]].append(s[idx])
        return ''.join([''.join(s_per_row) for s_per_row in summarized_s])

