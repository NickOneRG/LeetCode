from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        stoper = {4:True, 16:True, 37:True, 58:True, 89:True,145:True,42:True,20:True}
        while n != 1:
            if stoper.get(n):
                return False
            s = 0
            for i in str(n):
                s += (int(i)**2)
            n = s  
        return True
# @lc code=end


m = Solution()

time = t.hisobla()
print(m.isHappy(19))
# print(call)  
print(t.hisobla(time,1))

