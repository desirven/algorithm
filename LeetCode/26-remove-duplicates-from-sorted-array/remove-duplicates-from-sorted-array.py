class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = len(nums)
        remove_num = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                remove_num.append(nums[i])
        for n in remove_num:
            nums.remove(n)
            nums.append("_")
            k -= 1
        return k