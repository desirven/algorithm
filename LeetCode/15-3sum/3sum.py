class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        for i in range(len(nums)-2):
            if nums[i]>0:
                break   # 가장 작은 수가 양수면 이후도 다 양수
            if i>0 and nums[i]==nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l<r:
                total = nums[i]+nums[l]+nums[r]
                if total<0:
                    l += 1
                elif total>0:
                    r -= 1
                else:
                    answer.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while 0<l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r<len(nums)-1 and nums[r] == nums[r+1]:
                        r -= 1
        return answer
