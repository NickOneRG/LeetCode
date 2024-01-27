from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        res = [1]
        for i in range(1, rowIndex//2+1):
            res.append((res[i-1] * ((rowIndex+1) - i)) // i)
        rowIndex += 1
        return res + res[::-1][rowIndex % 2 :]
    

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.getRow(4))
# print(call)  
print(t.hisobla(time,1))
