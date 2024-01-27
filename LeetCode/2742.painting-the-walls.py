from TestTime import TimeSet
from typing import List
t = TimeSet()

#
# @lc app=leetcode id=2742 lang=python3
#
# [2742] Painting the Walls
#

    
# class Solution:
#     def paintWalls(self, cost: List[int], time: List[int]) -> int:
#         len_all = len(cost)
#         res = [2**35] * (len_all + 1)
#         res[0] = 0
#         for i in range(len_all):
#             for z in range(len_all, 0, -1):
#                 res[z] = min(
#                     res[z],
#                     res[max(z - time[i] - 1, 0)] + cost[i]
#                 )
#         return res[len_all]




# @lc code=start
from functools import lru_cache
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        @lru_cache(maxsize=None)
        def dp(i, remain):
            if remain <= 0:return 0
            if i == n:return float('inf')  
            
            paint = cost[i] + dp(i + 1, remain - 1 - time[i])
            dont_paint = dp(i + 1, remain)
            return min(paint, dont_paint)
    
        n = len(cost)
        return dp(0, n)

# @lc code=end

m = Solution()

time = t.hisobla()
print(m.paintWalls([26,53,10,24,25,20,63,51,5],[1,1,1,1,2,2,2,1,2]))
# print(call)  
print(t.hisobla(time,1))


# class Solution:
#     def paintWalls(self, cost: List[int], time: List[int]) -> int:
#         n = len(cost)
#         dp = [float('inf')] * (n + 1)
#         print(dp)
#         dp[0] = 0

#         for i in range(n):
#             for j in range(n, 0, -1):
#                 dp[j] = min(dp[j], dp[max(j - time[i] - 1, 0)] + cost[i])

#         return dp[n]