class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        last_num = nums[0]
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i]==last_num:
                if cnt<2:
                    cnt += 1
                    k += 1
                else:
                    cnt += 1
                    nums[i] = 10001
            else:
                last_num = nums[i]
                cnt = 1
                k += 1
        nums.sort()
        return k