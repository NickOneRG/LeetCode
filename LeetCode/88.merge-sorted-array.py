from typing import List 
#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n: 
            for i in range(m, m+n):
                nums1[i] = nums2.pop()
            nums1.sort()
        return nums1

# @lc code=end

m = Solution()
print(m.merge([1, 2,3,0,0,0], 3, [2,5,6], 3))