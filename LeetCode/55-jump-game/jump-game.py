class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current = len(nums)-1
        for prev in range(len(nums)-1, -1, -1):
            if current-prev <= nums[prev]:
                current = prev
            if current == 0:
                return True
        return False