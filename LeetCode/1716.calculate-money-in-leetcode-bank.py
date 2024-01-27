from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1716 lang=python3
#
# [1716] Calculate Money in Leetcode Bank
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        res, monday = 0, 0
        
        for i in range(1, n + 1):
            if i % 7 == 0:
                res += (monday + 7)
                monday += 1

            else: res += (monday + i % 7)
                

        return res


        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.totalMoney(20))
# print(call)
print(t.hisobla(time, 1))