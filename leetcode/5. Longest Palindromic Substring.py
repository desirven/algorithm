class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindromic(left, right) -> bool:
            right -=1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for length in range(len(s), 0, -1):
            for start in range(len(s)-length+1):
                if is_palindromic(start, start+length):
                    return s[start: start+length]

        return ""

'''
다른 사람 것 보고 배운 코드 : 안쪽에서 바깥쪽으로 하는 방법도 있네...
3903ms => 380ms로 훨씬 빨라짐
생각해보면 solution1은 최악이 O(n^3)인데, solution2는 최악이 O(n^2)임
데이터에 따라 다르긴 하겠지만 solution2가 더 효율적임
'''

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        def find_pal(s, left, right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left, right = left-1, right+1
            return s[left+1:right]

        pal = ""
        for i in range(len(s)):
            left, right = i, i #odd case
            tmp_pal = find_pal(s, left, right)
            if len(pal)<len(tmp_pal):
                pal=tmp_pal

            right += 1
            tmp_pal = find_pal(s, left, right)
            if len(pal)<len(tmp_pal):
                pal=tmp_pal
        return pal
