class Solution:
    def trap(self, height: List[int]) -> int:
        peak_val = 0
        trap_amount, tmp = 0, 0
        for i in range(len(height)):
            if height[i] >= peak_val:
                trap_amount += tmp
                tmp = 0
                peak_val = height[i]
            else:
                tmp += peak_val-height[i]

        peak_val, tmp = height[-1], 0
        for i in range(len(height)-1,-1,-1):
            if height[i] > peak_val:
                trap_amount += tmp
                tmp = 0
                peak_val = height[i]
            else:
                tmp += peak_val-height[i]
        return trap_amount