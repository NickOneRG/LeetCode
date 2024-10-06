from typing import List
#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        res = 0

        while left < right:
            res = max(res, (right - left)* min(height[left], height[right]))

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return res
    
# @lc code=end

m = Solution()
print(m.maxArea([1, 8,6,2,5,4,8,3,7]))