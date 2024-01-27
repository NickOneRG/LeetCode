from TestTime import TimeSet
from typing import List
t = TimeSet()
# 
# @lc app=leetcode id=275 lang=python3
#
# [275] H-Index II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:

        for ind, citation in enumerate(citations[::-1]):
            if ind >= citation: return ind
                
        return len(citations)
        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.hIndex([0, 1, 3, 5, 6]))
# print(call)
print(t.hisobla(time, 1))
