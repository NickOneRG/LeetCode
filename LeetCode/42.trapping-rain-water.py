from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        s = 0
        checker = True
        for ind, val in enumerate(height):

            if checker and ind > 0 and val > height[ind-1]:
                checker = True
                if 
                s += val - val 
        pass
# @lc code=end


# inp = int(input("Enter = "))
m = Solution()
time = t.hisobla()

print(m.trap([0,1,0,2,1,0,1,3,2,1,2,1]),t.hisobla(time, 1))