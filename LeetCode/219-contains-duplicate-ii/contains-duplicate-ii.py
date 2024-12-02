class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = defaultdict(list)
        for i in range(len(nums)):
            index_map[nums[i]].append(i)
        
        for vals in index_map.values():
            if len(vals) < 2:
                continue
            for i in range(len(vals)-1):
                if vals[i+1]-vals[i] <= k:
                    return True
        
        return False
