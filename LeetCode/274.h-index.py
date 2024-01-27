from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=274 lang=python3
#
# [274] H-Index
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True) 
        for ind, citation in enumerate(citations):
            if ind >= citation: return ind
                
        return len(citations)
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.hIndex([1]))
# print(call)
print(t.hisobla(time, 1))

