class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        count = 1
        current_idx = 0
        current_jump_max = nums[0]
        next_jump_max = 0
        while current_jump_max < len(nums)-1:
            for idx in range(current_idx+1, current_jump_max+1):
                next_jump_max = max(next_jump_max, idx+nums[idx])
            current_idx = current_jump_max
            current_jump_max = next_jump_max
            count += 1

        return count