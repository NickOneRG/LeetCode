from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#

# @lc code=start    
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one, two = 0, 0
        for i in range(2, len(cost) + 1):
            one, two = two, min(two + cost[i - 1], one + cost[i - 2])

        return two

# @lc code=end

m = Solution()

time = t.hisobla()
print(m.minCostClimbingStairs([10,15,20,10]))
# print(call)  
print(t.hisobla(time,1))