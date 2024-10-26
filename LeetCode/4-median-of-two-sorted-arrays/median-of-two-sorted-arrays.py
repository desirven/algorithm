# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        i_start, i_end = 0, len(nums1)
        half_length = (len(nums1) + len(nums2) + 1)//2
        while i_start<=i_end:
            i = (i_start+i_end)//2
            j = half_length - i
            if i < len(nums1) and nums1[i] < nums2[j-1]:
                i_start = i+1
            elif i > 0 and nums1[i-1] > nums2[j]:
                i_end = i-1
            else:
                if i == 0:
                    left_max = nums2[j-1]
                elif j == 0:
                    left_max = nums1[i-1]
                else:
                    left_max = max(nums1[i-1], nums2[j-1])

                if (len(nums1)+len(nums2))%2:
                    return left_max

                if i == len(nums1):
                    right_min = nums2[j]
                elif j == len(nums2):
                    right_min = nums1[i]
                else:
                    right_min = min(nums1[i], nums2[j])
                return (left_max + right_min)/2.0
        return 0.0