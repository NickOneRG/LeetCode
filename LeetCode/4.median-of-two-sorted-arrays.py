#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: [int], nums2:[int]) -> float:
        nums1 = sorted(nums1 + nums2)
        return (nums1[len(nums1) // 2] + nums1[(len(nums1) - 1) // 2]) / 2

# @lc code=end
        nums1 = sorted([*nums1, *nums2])
        print(nums1)
        if len(nums1) == 1:
            return nums1[0]
        if len(nums1)%2==0:
            l = (nums1[(int(len(nums1)/2)-1)] + nums1[int(len(nums1)/2)])/2
            
        return l if len(nums1)%2==0 else nums1[int((len(nums1)+1)/2-1)]
m = Solution()
print(m.findMedianSortedArrays([0,0], [0,0]))