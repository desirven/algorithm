class Solution:
    def romanToInt(self, s: str) -> int:
        values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = values[s[-1]]
        for i in range(1, len(s)):
            if values[s[i]] > values[s[i-1]]:               
                result -= values[s[i-1]]
            else:
                result += values[s[i-1]]
        return result