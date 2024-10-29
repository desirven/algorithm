class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        interval = int(len(nums)/2)
        i = 0
        while i < len(nums):
            if nums[i]==nums[i+interval]:
                return nums[i]
            else:
                i += 1