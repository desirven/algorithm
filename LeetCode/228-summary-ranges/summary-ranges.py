class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []
        if len(nums)==0:
            return answer
        
        tmp = nums[0]
        for i in range(len(nums)-1):
            if nums[i]+1<nums[i+1]:
                if tmp == nums[i]:
                    answer.append(str(tmp))
                else:
                    answer.append(f"{tmp}->{nums[i]}")
                tmp = nums[i+1]
        if tmp == nums[-1]:
            answer.append(str(tmp))
        else:
            answer.append(f"{tmp}->{nums[-1]}")
        return answer