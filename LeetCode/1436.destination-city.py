from TestTime import TimeSet
from typing import List
t = TimeSet()

# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

# @lc code=start
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        left, right = zip(*paths)
        
        return (set(right) - set(left)).pop()
        
        
# @lc code=end


m = Solution()
time = t.hisobla()
print(m.destCity([["B","C"],["D","B"],["C","A"]]))
# print(call)
print(t.hisobla(time, 1))

print(*zip('abcdefg', range(6), range(2,8)))  # learning how zip() is working

# class Solution:
#     def destCity(self, paths: List[List[str]]) -> str:
#         res, ros = paths[0][0], paths[-1][1]
        
#         left, right = zip(*paths)
#         res = list((set(left).symmetric_difference(set(right))))
        
#         return ros if ros in res else res.remove(ros)
