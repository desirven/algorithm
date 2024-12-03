class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        numset = set(nums)
        for num in nums:
            if num-1 not in numset:
                cur = num
                cnt = 1
                while cur + 1 in numset:
                    cnt += 1
                    cur += 1
                answer = max(answer, cnt)
        return answer