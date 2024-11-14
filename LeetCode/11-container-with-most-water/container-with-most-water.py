class Solution:
    def maxArea(self, height: List[int]) -> int:
        answer = 0
        l, r = 0, len(height)-1
        while l<r:
            if height[l] > height[r]:
                answer = max(answer, height[r]*(r-l))
                r -= 1
            else:
                answer = max(answer, height[l]*(r-l))
                l += 1
        return answer