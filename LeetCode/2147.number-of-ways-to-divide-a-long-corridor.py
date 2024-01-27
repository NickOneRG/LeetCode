from TestTime import TimeSet
from typing import List
t = TimeSet()
#
# @lc app=leetcode id=2147 lang=python3
#
# [2147] Number of Ways to Divide a Long Corridor
#

# @lc code=start
class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seats, memo, ways = 0, 0, 1
        
        for ind, val in enumerate(corridor):
            if val == "S":

                if seats < 2: seats += 1
                else:
                    seats = 1
                    ways *= (ind - memo)

                memo = ind

        return 0 if seats < 2 else ways % (10 ** 9 + 7)

# @lc code=end


m = Solution()
time = t.hisobla()
print(m.numberOfWays("SSPPSPSPPSS"))
# print(call)  
print(t.hisobla(time,1))

# class Solution:
#     def numberOfWays(self, corridor):
#         MOD = 10**9 + 7
#         zero, one, two = 0, 0, 1

#         for i in corridor:
#             if i == 'S': 
#                 one, two, zero = two, one, one
#             else:    two       =(two + zero) % MOD
                
#         return zero
    
