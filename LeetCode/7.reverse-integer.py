from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
            
        x  *= sign
        res = sign * int(str(x)[::-1])
        
        return 0 if  2**31 -1 < res or res < -2**31 else res
        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.reverse(-5463847412))
# print(call)  
print(t.hisobla(time,1))
print(6 in range(6,10))