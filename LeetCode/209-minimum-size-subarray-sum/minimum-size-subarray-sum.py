class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        total, r = 0, 0
        answer = len(nums)
        for l in range(len(nums)):
            while total < target and r < len(nums):
                total += nums[r]
                r += 1
            if total >= target:
                answer = min(answer, r-l)
            total -= nums[l]
        return answer