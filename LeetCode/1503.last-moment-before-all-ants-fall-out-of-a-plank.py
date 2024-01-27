from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=1503 lang=python3
#
# [1503] Last Moment Before All Ants Fall Out of a Plank
#

# @lc code=start
class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        res = 0
        for i in list(left):  res = max(res, abs(0 - i))
        for i in list(right): res = max(res, abs(n - i))
        
        return res

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.getLastMoment( 4, [4,3], [0,1]))
# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
#         return max(n-min(right+[n]), max(left+[0]))