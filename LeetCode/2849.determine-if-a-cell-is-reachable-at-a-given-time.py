from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2849 lang=python3
#
# [2849] Determine if a Cell Is Reachable at a Given Time
#

# @lc code=start
class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == sy == fx == fy:
            return (t > 0 or t == 0)

        return t >= max(abs(fx - sx), abs(fy - sy))
        
# @lc code=end

m = Solution()
time = t.hisobla()
print(m.isReachableAtTime(1, 1, 1, 2, 1))
# print(call)  
print(t.hisobla(time,1))
