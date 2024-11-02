class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # reference: https://youtu.be/5bS636lE_R0
        total_len = len(nums)
        answer = [1]*total_len
        for idx in range(1, total_len):
            answer[idx] = answer[idx-1]*nums[idx-1]
        tmp = nums[-1]
        for idx in range(total_len-2, -1, -1):
            answer[idx] *= tmp
            tmp *= nums[idx]
        return answer