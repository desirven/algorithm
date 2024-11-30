class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        l, r = 0, len(nums)-1
        while True:
            if sorted_nums[l]+sorted_nums[r] == target:
                break
            elif sorted_nums[l]+sorted_nums[r] > target:
                r -= 1
            else:
                l += 1

        answer = []
        for i in range(len(nums)):
            if nums[i] == sorted_nums[l] or nums[i] == sorted_nums[r]:
                answer.append(i)
            if len(answer)==2:
                return answer